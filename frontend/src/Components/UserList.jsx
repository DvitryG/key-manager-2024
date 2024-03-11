import React from 'react';
import { useNavigate } from 'react-router-dom';
import "../Styles/index.css";
import '../Styles/button.css';

const UserList = ({ fullName, email, status, user_id }) => {
    const navigate = useNavigate();

    const handleClick = () => {
        // Redirect to the /users route and pass user details as URL parameters
        navigate(`/users?user_id=${user_id}&fullName=${encodeURIComponent(fullName)}&email=${encodeURIComponent(email)}&roles_str=${encodeURIComponent(status)}`);
    };

    return (
        <>
        <div className='d-flex mb-2 line' onClick={handleClick} style={{ cursor: 'pointer' }}>
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
