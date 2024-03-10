import React, { useState, useEffect } from 'react';
import axios from 'axios';
import UserList from '../Components/UserList';

function UserListPage (){
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchUsers = async () => {
            try {
                const accessToken = localStorage.getItem('accessToken');
                const response = await axios.get('http://0.0.0.0:5000/users/?page=0&page_size=10', {
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                        'accept': 'application/json'
                    }
                });
                setUsers(response.data.users);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching users:', error);
                setError('Error fetching users. Please try again.');
                setLoading(false);
            }
        };

        fetchUsers();
    }, []);

    return (
        <div>
            <div className="request-header p-4 ps-5">
                <h1>Список пользователей</h1>
            </div>
            <div className="container d-flex justify-content-center flex-column w-75">
                {loading ? (
                    <p>Loading...</p>
                ) : error ? (
                    <p>{error}</p>
                ) : (
                    <div>
                        {users.map(user => (
                            <UserList
                                key={user.user_id}
                                fullName={user.name}
                                email={user.email}
                                status={user.roles_str}
                            />
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}

export default UserListPage;
