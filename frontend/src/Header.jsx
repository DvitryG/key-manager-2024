import React from 'react';
import { Button } from 'react-bootstrap';
import "./index.css";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';



const Header = () => {
    return (
          <Navbar bg="dark" data-bs-theme="dark">
            <Container>
              <Navbar.Brand href="#home">Key</Navbar.Brand>
              <Nav className="me-auto">
                <Nav.Link href="#home">Заявки</Nav.Link>
                <Nav.Link href="#features">Ключи</Nav.Link>
              </Nav>
              <Nav>
              <Nav.Link href="#pricing">Войти</Nav.Link>
              </Nav>
            </Container>
          </Navbar>
      );
}

export default Header;
