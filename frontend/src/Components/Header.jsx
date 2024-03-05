import React from 'react';
import "../index.css";
import "../App.css";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom';
import '../Styles/index.css'


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
                <Link to="/keys" className=''>Выданные ключи</Link>
              </Nav>
              <Nav>
              <Nav>
               <Link to="/login">Войти</Link> 
               </Nav>
              </Nav>
            </Container>
          </Navbar>
      );
}

export default Header;
