import React from 'react';
import "../Styles/index.css";
import '../Styles/button.css';


const KeysCard = ({ fullName, person }) => {
    return (
        <>
        <div className='d-flex justify-content-between mb-2 line'>
            <div className='d-flex flex-column'>
                <div className='mb-2 fw-semibold'>{fullName} </div>
                <div>{person}</div>
            </div>
                <div className='btn btn-good mb-3'>Подтвердить возврат</div>
        </div>
       </>
        
    );
};

export default KeysCard;