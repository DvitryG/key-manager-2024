import React from 'react';
import "../index.css";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom';

const Header = () => {
    return (
          <Navbar bg="dark" data-bs-theme="dark">
            <Container>
              <Navbar.Brand>
               <Link to="/keys">Выданные ключи</Link>
               </Navbar.Brand>
              <Nav className="me-auto">
                <Link to="/requests">Заявки</Link>
                <Nav.Link href="#features">Пользователи</Nav.Link>
                <Nav.Link href="#feature">Кабинеты</Nav.Link>
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
