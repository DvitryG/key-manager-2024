import React from 'react';
import "../index.css";
import "../App.css";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom';
import '../Styles/index.css'
import EditUser from '../Pages/EditUser';


const Header = () => {
    return (
      
          <Navbar bg="navbar" data-bs-theme="dark">
            <Container>
              {/* <Navbar.Brand>
               <Link to="/keys">Выданные ключи</Link>
               </Navbar.Brand> */}
              <Nav className="me-auto">
                <Link to="/requests" className='me-2'>Заявки</Link>
                <Link to="/list" className='me-2'>Пользователи</Link>
                <Link to="/office" className='me-2'>Кабинеты</Link>
                <Link to="/keys" className='me-2'>Выданные ключи</Link>
                <Link to="/profile" className='me-2'>Профиль</Link>
                <Link to="/users" className='me-2'>редактировать пользователя</Link>
              </Nav>
              <Nav>
              <Nav>
               <Link to="/login" className='me-2'>Войти</Link>
               <Link to="/registration" className='me-2'>Регистрация</Link> 
               </Nav>
              </Nav>
            </Container>
          </Navbar>
      );
}

export default Header;
