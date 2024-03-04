import React from 'react';
import "../Styles/index.css";
import '../Styles/button.css';

const CardComponent = ({ fullName, room, date, status }) => {
    return (
        <>
        <div className='d-flex justify-content-between mb-2 line'>
            <div className='d-flex flex-column'>
                <div className='mb-2 fw-semibold'>{fullName} </div>
                <div>{room} + {date}</div>
            </div>
            <div className='d-flex flex-row p-2'>
                {status == 'good' ? (
                  <div className='btn btn-outline-danger'>Закрыть</div> )
                   : ( <>
                  <div className='btn btn-done me-2'>Одобрить</div>
                  <div className='btn btn-outline-danger'>Закрыть</div>
                  </> )
                  }
              
            </div>
        </div>
       </>
        
    );
};

export default CardComponent;