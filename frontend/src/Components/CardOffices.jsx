import React, { useState } from 'react';
import axios from 'axios';
import Form from "react-bootstrap/Form";
import { useNavigate } from 'react-router-dom';
import Input from './Input';
import "../Styles/index.css";
import '../Styles/button.css';
import {url} from "../url.js";

const CardOffices = () => {
  const [name, setName] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const createRoom = async (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    setName(event.target.value);
    const accessToken = localStorage.getItem('accessToken');
    const roomName = name; // Get the room name from the state variable

    try {
      const response = await axios.post(
        `${url}/rooms/`,
        {
          name: roomName,
        },
        {
          headers: {
            'Authorization': `Bearer ${accessToken}`,
            Accept: "application/json",
            "Content-Type": "application/json",
          },
        }
      );

      console.log("Room created successfully:", response.data);
      // Update UI or perform other actions as needed
      navigate('/office'); // Navigate to home page after successful room creation
    } catch (error) {
      console.error("Error creating room:", error);
      setError("Error while creating room. Please try again.");
    }
  };

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  return (
    <div className="mt-3 me-3 mb-4">
      {error && <p className="text-danger">{error}</p>}
      <Form className="card mt-0">
        <div className='container d-flex justify-content-center'>
          <div className='request-form d-flex flex-column'>
            <div className="d-flex flex-column">
              <Input title="Создать кабинет" placeholder="Новый кабинет" onChange={handleNameChange} value={name}></Input>
            </div>
            <div className='d-flex flex-row '>
              <button className='btn btn-good' onClick={createRoom}>Создать</button>
            </div>
          </div>
        </div>
      </Form>
    </div>
  );
};

export default CardOffices;
