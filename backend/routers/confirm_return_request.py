from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import Session, select
from starlette import status

from backend.dependencies.database import get_db_session
from backend.dependencies.user import authorize
from backend.models.common import Pagination
from backend.models.confirm_receipt_request import ConfirmReceiptRequest
from backend.models.confirm_return_request import ConfirmReturnRequest
from backend.models.user import Role
from backend.tools.common import get_filtered_items, get_pages_count_from_cache, get_filtered_count
from backend.tools.obligation import RequestsCache, RequestsListResponse

router = APIRouter(
    prefix="/confirm_return_requests",
    tags=["confirm_return_request"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", dependencies=[Depends(
    authorize(Role.ADMIN, Role.DEAN))
])
async def get_all_confirm_return_requests(
        db_session: Annotated[Session, Depends(get_db_session)],
        page: Annotated[int, Query(ge=0)] = 0,
        page_size: Annotated[int, Query(ge=1, le=100)] = 10,
) -> RequestsListResponse:
    requests = db_session.exec(
        select(ConfirmReceiptRequest).where(ConfirmReceiptRequest.confirmed == True)
        .offset(page * page_size)
        .limit(page_size)
    ).all()

    pages_count = db_session.query(ConfirmReceiptRequest).count()

    return RequestsListResponse(
        requests=requests,
        pagination=Pagination(
            page_size=len(requests),
            pages_count=pages_count,
            current_page=page
        )
    )


@router.put("/{request_id}", dependencies=[Depends(
    authorize(Role.ADMIN, Role.DEAN))
])
async def confirm_return(
        db_session: Annotated[Session, Depends(get_db_session)],
        request_id: UUID
):
    request = db_session.get(ConfirmReceiptRequest, request_id)
    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The request with request_id: {request_id} not found in the system."
        )
    db_session.delete(request)
    db_session.commit()

