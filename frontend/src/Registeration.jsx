import React from "react";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import "./style.css";

const Registeration = () => {
  return (
    <Container className="mt-3">
      <Form className="reg">
      <h1 className="textTitle">Регистрация</h1>
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
        <Button className="logbtn" variant="primary" type="submit">
          Зарегистроваться
        </Button>
        </div>
      </Form>
    </Container>
  );
};

export default Registeration;
