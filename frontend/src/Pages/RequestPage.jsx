import React, {useEffect, useState} from 'react';
import RequestForm from '../Components/RequestForm';
import Card from '../Components/Card';
import axios from "axios";
import {url} from "../url";
import UserList from "../Components/UserList";



const RequestPage = () => {
    const [orders, setOrders] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');


    useEffect(() => {
        const fetchUsers = async () => {
            try {
                const accessToken = localStorage.getItem('accessToken');
                const response = await axios.get(`${url}/orders/all`, {
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                        'accept': 'application/json'
                    }
                });
                setOrders(response.data.orders);
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
                <h1>Список заявок</h1>
            </div>
          <RequestForm />
          <div className="container d-flex justify-content-center flex-column w-75">

              {loading ? (
                  <p>Loading...</p>
              ) : error ? (
                  <p>{error}</p>
              ) : (
                  <div>
                      {orders.map(order => (
                          <Card fullName={order.user.name} room={order.room.name} date={order.day} status={order.status}/>
                      ))}
                  </div>
              )}
          </div>
     
        </div>
    );
}

export default RequestPage;

