import React from 'react';
import "../Styles/index.css";
import '../Styles/button.css';

const ListOffices = ({room, available}) => {
    return (
        <>
        <div className='d-flex justify-content-between mb-2 line'>
            <div className='d-flex flex-column'>
                <div className='d-flex w-50 justify-content-start'>Кабинет: {room}</div>
            </div>
            { available ? 
                    <div className='btn btn-bad mb-3 w-25'>Сделать недоступным</div>
                    : <div className='btn btn-good mb-3 w-25'>Сделать доступным</div> 
            }
                {/* <div className='btn btn-bad mb-3 w-25'>Сделать недоступным</div> */}
        </div>
       </>
    );
}

export default ListOffices;
