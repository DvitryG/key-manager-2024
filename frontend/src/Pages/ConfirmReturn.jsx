import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ConfirmReturnRequests() {
  const [requests, setRequests] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchRequests = async () => {
      try {
        const accessToken = localStorage.getItem('accessToken');
        const response = await axios.get('http://0.0.0.0:5000/confirm_return_requests/?page=0&page_size=10', {
          headers: {
            'Authorization': `Bearer ${accessToken}`,
            'accept': 'application/json'
          }
        });
        setRequests(response.data.requests);
      } catch (error) {
        console.error('Error fetching confirm return requests:', error);
        setError('Error fetching confirm return requests. Please try again.');
      }
    };

    fetchRequests();
  }, []);

  const handleConfirm = async (roomId) => {
    try {
      const accessToken = localStorage.getItem('accessToken');
      await axios.delete(`http://0.0.0.0:5000/confirm_return_requests/${roomId}`, {}, {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'accept': 'application/json'
        }
      });
      // Remove the confirmed request from the list
      setRequests(requests.filter(request => request.room.room_id !== roomId));
      // Handle success or update UI as needed
    } catch (error) {
      console.error('Error confirming return request:', error);
      // Handle error or show error message
    }
  };

  return (
    <div>
        <div className="request-header p-4 ps-5">
                <h1>выданные ключи</h1>
            </div>
      {error && <p>{error}</p>}
      {requests.map(request => (
        <div key={request.room.room_id}>
          <p>User: {request.user.name}</p>
          <p>Room: {request.room.name}</p>
          <button onClick={() => handleConfirm(request.room.room_id)}>Confirm</button>
        </div>
      ))}
    </div>
  );
}

export default ConfirmReturnRequests;
