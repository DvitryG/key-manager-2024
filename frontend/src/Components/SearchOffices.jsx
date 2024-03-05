import React from 'react';
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Input from './Input';
import "../Styles/index.css";
import '../Styles/button.css';


const CardOffices = () => {
        return (
            <div className="mt-3">
                 <Form className="search mt-0">
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
                      
                            <div className='h-50 align-self-center'>
                                <button className='btn btn-search d-flex align-items-end mb-2'>Искать</button>
                            </div>
                        </div>
                    </div>
                 </Form>
            </div>
        );
};

export default CardOffices;