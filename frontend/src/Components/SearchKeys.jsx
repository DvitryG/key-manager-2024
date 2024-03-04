import React from 'react';
import Input from './Input';
import "../Styles/index.css";

const SearchKeys = () => {
    return (
        <div className='container d-flex justify-content-center'>
        <div className='request-form d-flex flex-row'>
            <div className="d-flex flex-column">
                <Input title="Пользователь" placeholder="Введите имя"></Input>
            </div>
            <div className='d-flex flex-column'>
                <Input title="Кабинет" placeholder="Номер кабинета"></Input>
            </div>
            <div className='d-flex align-items-end mb-2'><button className='btn btn-search'>Искать</button></div>
        </div>
    </div>
    );
}

export default SearchKeys;
