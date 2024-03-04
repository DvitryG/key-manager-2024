import React from 'react';
import Input from './Input';

const RequestForm = () => {
    return (
        <div className='container d-flex justify-content-center'>
        <div className='request-form d-flex flex-row'>
            <div className="d-flex flex-column">
                <Input title="Пользователь" placeholder="Введите имя"></Input>
                <Input title="Дата" placeholder="Дата"></Input>
            </div>
            <div className='d-flex flex-column'>
                <Input title="Статус заявки" placeholder="Статус"></Input>
                <Input title="Кабинет" placeholder="Номер кабинета"></Input>
            </div>
            <div className='d-flex align-items-end mb-2'><button className='btn btn-success'>Искать</button></div>
        </div>
    </div>
    );
}

export default RequestForm;
