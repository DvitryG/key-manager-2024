import React, { useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Logout() {
  const navigate = useNavigate();

  useEffect(() => {
    const logout = async () => {
      try {
        const accessToken = localStorage.getItem('accessToken');
        await axios.delete('http://0.0.0.0:5000/users/logout', {
          headers: {
            'Authorization': `Bearer ${accessToken}`,
            'accept': 'application/json'
          }
        });
        // Logout successful, navigate to login page
        navigate('/login');
      } catch (error) {
        console.error('Error logging out:', error);
        navigate('/login');
      }
    };

    logout(); // Start logout process when component mounts
  }, [navigate]); // Empty dependency array ensures the effect runs only once when component mounts

  return (
    <div>
      <p>Logging out...</p>
    </div>
  );
}

export default Logout;
