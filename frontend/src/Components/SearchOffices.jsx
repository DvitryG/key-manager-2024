import React from 'react';
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Input from './Input';
import "../Styles/index.css";
import '../Styles/button.css';


const CardOffices = () => {
        return (
            <div className="mt-3">
                 <Form className="search">
                    <div className='container d-flex justify-content-center'>
                     <div className='request-form d-flex flex-row'>
                       <div className="d-flex flex-column">
                         <Input title="Поиск" placeholder="Новый кабинет"></Input>

                         <div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    доступность
                    </button>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#">Все</a></li>
                        <li><a class="dropdown-item" href="#">Доступные action</a></li>
                        <li><a class="dropdown-item" href="#">Недоступные</a></li>
                    </ul>
                    </div>
                        </div>
                      
                            <div className='d-flex flex-row-reverse p-4'>
                                <button className='btn btn-search'>Искать</button>
                            </div>
                        </div>
                    </div>
                 </Form>
            </div>
        );
};

export default CardOffices;