import React, {useState} from 'react';
import axios from 'axios';
import Form from "react-bootstrap/Form";
import Input from './Input';
import "../Styles/index.css";
import '../Styles/button.css';


const CardOffices = () => {
    const [name, setName] = useState("");
    const [error, setError] = useState("");
    
    const searchRoom = async (event) => {
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
        
        console.log("searched successfully:", response.data);
      } catch (error) {
        console.error("searching error:", error);
        setError("Error while searching. Please try again.");
      }
    };
    const handleNameChange = (event) => {
      setName(event.target.value);
    };
        return (
            <div className="mt-3">
                {error && <p className="text-danger">{error}</p>}
                 <Form className="search mt-0">
                    <div className='container d-flex justify-content-center'>
                     <div className='request-form d-flex flex-row'>
                       <div className="d-flex flex-column">
                         <Input title="Поиск" value={name} onChange={handleNameChange} placeholder="Новый кабинет"></Input>

                         <div className="dropdown">
  <button className="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    доступность
                    </button>
                    <ul className="dropdown-menu">
                        <li><a className="dropdown-item" href="#">Все</a></li>
                        <li><a className="dropdown-item" href="#">Доступные action</a></li>
                        <li><a className="dropdown-item" href="#">Недоступные</a></li>
                    </ul>
                    </div>
                        </div>
                      
                            <div className='h-50 align-self-center'>
                                <button onClick={searchRoom} className='btn btn-search d-flex align-items-end mb-2'>Искать</button>
                            </div>
                        </div>
                    </div>
                 </Form>
            </div>
        );
};

export default CardOffices;