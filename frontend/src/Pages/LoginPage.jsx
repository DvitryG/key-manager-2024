import React from 'react';
import Header from '../Components/Header';
import Login from '../Components/Login';
const LoginPage = () => {
    return (
        <>
        <div className="request-header p-4 ps-5">
                <h1>Вход</h1>
        </div>
         <Login />
        </>
    );
}

export default LoginPage;
