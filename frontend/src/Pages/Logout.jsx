import React, { useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import {url} from "../url.js";
function Logout() {
  const navigate = useNavigate();

  useEffect(() => {
    const logout = async () => {
      try {
        const accessToken = localStorage.getItem('accessToken');
        await axios.delete(`${url}/users/logout`, {
          headers: {
            'Authorization': `Bearer ${accessToken}`,
            'accept': 'application/json'
          }
        });
        localStorage.removeItem('accessToken');
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
