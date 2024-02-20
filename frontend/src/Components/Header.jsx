import React from 'react';
import "../index.css";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import LoginPage from '../Pages/LoginPage';
import { Link } from 'react-router-dom';

const Header = () => {
    return (
          <Navbar bg="dark" data-bs-theme="dark">
            <Container>
              <Navbar.Brand>
               <Link to="/">Key</Link>
               </Navbar.Brand>
              <Nav className="me-auto">
                <Nav.Link href="#home">Заявки</Nav.Link>
                <Nav.Link href="#features">Ключи</Nav.Link>
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
