import React from "react";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import "../Styles/styleYusuf.css";
import { Link } from "react-router-dom";


const Registration = () => {
  return (
    <Container className="mt-3 w-50">
      <Form className="reg">
      <Form.Group className="mb-3" controlId="formBasicEmail">
          <h6 className="textTitle">ФИО</h6>
          <Form.Control type="text" placeholder="Иванов Иван Иванович" />
        </Form.Group>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <h6 className="textTitle">Email</h6>
          <Form.Control type="email" placeholder="name@example.com" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <h6 className="textTitle">Пароль</h6>
          <Form.Control type="password"/>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <h6 className="textTitle">Повторите пароль</h6>
          <Form.Control type="password"/>
        </Form.Group>
        <div>
        <Button className="acc mb-3 d-grid gap-2 col-6 mx-auto">
          <Link to="/login">Уже есть аккаунт?</Link> 
        </Button>
        <Button className="regist mb-3 d-grid gap-2 col-6 mx-auto">
          Зарегистроваться
        </Button>
        </div>
      </Form>
    </Container>
  );
};

export default Registration;
