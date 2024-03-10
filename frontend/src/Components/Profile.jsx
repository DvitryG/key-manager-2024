import React, { useState, useEffect } from 'react';
import axios from 'axios';

import "../Styles/styleYusuf.css";

const Profile = () => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [old_password, setOld_Password] = useState('');
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            try {
                const accessToken = localStorage.getItem('accessToken');
                const response = await axios.get('http://0.0.0.0:5000/users/me', {
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                        'accept': 'application/json'
                    }
                });
                const userData = response.data;
                setName(userData.name);
                setEmail(userData.email);
            } catch (error) {
                console.error('Error fetching user data:', error);
                // Handle error fetching user data
            }
        };

        fetchData();
    }, []);
    
    const handleSaveChanges = async () => {
        try {
            const accessToken = localStorage.getItem('accessToken');
            const response = await axios.put(
                'http://0.0.0.0:5000/users/me',
                {
                    name: name,
                    email: email
                },
                {
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                        'Content-Type': 'application/json'
                    }
                }
            );
            setError('Profile changes saved successfully:', response.data);
            // Optionally, you can display a success message or redirect the user
        } catch (error) {
            if (error.response && error.response.data && error.response.data.detail) {
                console.error('Error saving profile changes:', error.response.data.detail);
                setError(error.response.data.detail);
            } else if (error.response) {
                console.error('Error saving profile changes:', error.response.data);
                setError('An error occurred while saving profile changes. Please try again.');
            } else {
                console.error('Error saving profile changes:', error);
                setError('An error occurred while saving profile changes. Please try again.');
            }
        }
    };

    const handleChangePassword = async () => {
        try {
            const accessToken = localStorage.getItem('accessToken');
            const response = await axios.put(
                'http://0.0.0.0:5000/users/me/password',
                {
                    old_password: old_password,
                    password: password 
                },
                {
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                        'Content-Type': 'application/json'
                    }
                }
            );
            setError('password was changed successfully:', response.data);
            
        } catch (error) {
            if (error.response && error.response.data && error.response.data.detail) {
                console.error('Error changing password:', error.response.data.detail);
                setError(error.response.data.detail);
            } else if (error.response) {
                console.error('Error changing password:', error.response.data);
                setError('An error occurred while changing password. Please try again.');
            } else {
                console.error('Error changing password:', error);
                setError('An error occurred while changing password. Please try again.');
            }
        }
    };
    return (
        <>
            <form>
            {error && <p className="text-danger login">{error}</p>}
                <div className='login'>
                    <div className='form-group'>
                        <h6 className="textTitle">ФИО</h6>
                        <input
                            className="inputText"
                            type="text"
                            placeholder='Иванов Иван Иванович'
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                        />
                        <h6 className="textTitle">Email</h6>
                        <input
                            className="inputText"
                            type="email"
                            placeholder='example@gmail.com'
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                        <button type="button" className='btn btn-search' onClick={handleSaveChanges}>Сохранить Изменение</button>
                    </div>
                </div>
            </form>

            <div className="form-group">
                <form className="login">
                    <h6 className="textTitle">Старый пароль</h6>
                    <input className="inputText"
                        type="password"
                        placeholder='Введите пароль'
                        value={old_password}
                        onChange={(e) => setOld_Password(e.target.value)}
                     />
                    <h6 className="textTitle">Новый пароль</h6>
                    <input 
                        className="inputText" 
                        type="password" 
                        placeholder='Повторите пароль'
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <button type="button" className='btn btn-search' onClick={handleChangePassword}>Сменить пароль</button>
                </form>
            </div>
            
        </>
    );
};

export default Profile;
