from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_users():
    pass


@router.post("/register")
async def register():
    pass


@router.post("/login")
async def login():
    pass


@router.post("/logout")
async def logout():
    pass


@router.get("/me")
async def read_me():
    pass


@router.put("/me")
async def update_me():
    pass


@router.put("/me/password")
async def update_my_password():
    pass


@router.put("/{user_id}")
async def update_user():
    pass
