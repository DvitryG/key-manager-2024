import React from 'react';
import "../Styles/index.css";
import '../Styles/button.css';


const UserList = ({ fullName, email, status }) => {
    return (
        <>
        <div className='d-flex mb-2 line'>
            <div className='d-flex flex-column w-50'>
                <div className='mb-2 fw-semibold'>{fullName} </div>
                <div>{email}</div>
            </div>
            <div className='d-flex w-50 justify-content-start align-items-center'>
                <div className='status'>{status} </div>
            </div>
        </div>
       </>
        
    );
};

export default UserList;