import React from "react";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import "../Styles/index.css";
import "../Styles/button.css";
import "../Styles/styleYusuf.css";
import { Link } from "react-router-dom";

const Login = () => {
  return (
    <Container className="mt-3">
      <Form className="login">
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <h6 className="textTitle">Email</h6>
          <Form.Control type="email" placeholder="name@example.com" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <h6 className="textTitle">Пароль</h6>

          <Form.Control type="password" placeholder="Password" />
        </Form.Group>
        <div>
        <Button className="logbtn d-grid gap-2 col-6 mx-auto" variant="secondary" type="submit">
          Войти
        </Button>
        <Button className="regbtn d-grid gap-2 col-6 mx-auto" variant="primary" type="submit">
           <Link to="/registration">Регистрация</Link> 
        </Button>
        </div>
      </Form>
    </Container>
  );
};

export default Login;
