import React from "react";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import "./style.css";
import { Link } from "react-router-dom";

const Login = () => {
  return (
    <Container className="mt-3">
      <Form className="login">
      <h1 className="textTitle">Вход</h1>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <h6 className="textTitle">Email</h6>
          <Form.Control type="email" placeholder="name@example.com" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <h6 className="textTitle">Пароль</h6>

          <Form.Control type="password" placeholder="Password" />
        </Form.Group>
        <div>
        <Button className="logbtn" variant="secondary" type="submit">
          Войти
        </Button>
        <Button className="logbtn" variant="primary" type="submit">
           <Link to="/registration" className="text">Регистрация</Link> 
        </Button>
        </div>
      </Form>
    </Container>
  );
};

export default Login;
