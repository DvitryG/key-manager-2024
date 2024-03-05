import React from 'react';
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Input from './Input';
import "../Styles/index.css";
import '../Styles/button.css';


const CardOffices = () => {
        return (
            <div className="mt-3 me-3">
                 <Form className="card">
                    <div className='container d-flex justify-content-center'>
                     <div className='request-form d-flex flex-column'>
                       <div className="d-flex flex-column">
                         <Input title="Создать кабинет" placeholder="Новый кабинет"></Input>
                      </div>
                <div className='d-flex flex-row-reverse p-4'><button className='btn btn-good'>Создать</button></div>
                     </div>
                 </div>
                 </Form>
            </div>
        );
};

export default CardOffices;