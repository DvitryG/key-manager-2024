import React from 'react';
import { Link } from 'react-router-dom';

function NotAuthenticatedPage() {
    return (
        <div className="container">
            
            <h2 className='mt-5'>Вы не авторизованы</h2>
            <p>Пожалуйста, войдите в систему или зарегистрируйтесь, чтобы получить доступ к этой странице.</p>
            <div>
                <Link to="/login" className="btn btn-primary">Login</Link>
                <Link to="/registration" className="btn btn-secondary">Register</Link>
            </div>
        </div>
    );
}

export default NotAuthenticatedPage;
