import React, { useState } from 'react';
import axios from 'axios';
import Form from "react-bootstrap/Form";
import Input from './Input';
import "../Styles/index.css";
import '../Styles/button.css';

const CardOffices = () => {

  const [name, setName] = useState("");
  const [error, setError] = useState("");
  
  const createRoom = async (event) => {
    try {
      const response = await axios.post(
        "http://0.0.0.0:5000/rooms/",
        {
          name: name,
        },
        {
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
        }
      );
      
      console.log("room created successfully:", response.data);
    } catch (error) {
      console.error("Creating error:", error);
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