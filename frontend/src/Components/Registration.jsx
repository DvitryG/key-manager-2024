import React, { useState } from "react";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { Link } from "react-router-dom";
import axios from "axios";
import "../Styles/styleYusuf.css";

const Registration = () => {
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");

  const handleFullNameChange = (event) => {
    setFullName(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleConfirmPasswordChange = (event) => {
    setConfirmPassword(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (password !== confirmPassword) {
      setError("Passwords do not match");
      return;
    }
    try {
      const response = await axios.post(
        "http://0.0.0.0:5000/users/register",
        {
          name: fullName,
          repeat_password: confirmPassword,
          email: email,
          password: password,
        },
        {
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
        }
      );
      // Registration successful
      console.log("Registration successful:", response.data);
      // Assuming the response contains an access token
      const { access_token } = response.data;
      // Store the access token in local storage or state for further use
      localStorage.setItem("accessToken", access_token);
      // Optionally, you can redirect the user to another page after successful registration
      // history.push("/dashboard");
    } catch (error) {
      if (error.response && error.response.data && error.response.data.detail) {
        setError(error.response.data.detail);
      } else {
        setError("Registration failed. Please try again.");
        console.error("Registration error:", error);
      }
    }
  };
  
  
  

  return (
    <Container className="mt-3 w-50">
      <Form className="reg" onSubmit={handleSubmit}>
        <Form.Group className="mb-3" controlId="formBasicFullName">
          <h6 className="textTitle">ФИО</h6>
          <Form.Control
            type="text"
            placeholder="Иванов Иван Иванович"
            value={fullName}
            onChange={handleFullNameChange}
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicEmail">
          <h6 className="textTitle">Email</h6>
          <Form.Control
            type="email"
            placeholder="name@example.com"
            value={email}
            onChange={handleEmailChange}
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <h6 className="textTitle">Пароль</h6>
          <Form.Control
            type="password"
            value={password}
            onChange={handlePasswordChange}
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicConfirmPassword">
          <h6 className="textTitle">Повторите пароль</h6>
          <Form.Control
            type="password"
            value={confirmPassword}
            onChange={handleConfirmPasswordChange}
          />
        </Form.Group>

        <div>
          <Button
            className="acc mb-3 d-grid gap-2 col-6 mx-auto"
            variant="secondary"
          >
            <Link to="/login">Уже есть аккаунт?</Link>
          </Button>
          <Button
            className="regist mb-3 d-grid gap-2 col-6 mx-auto"
            variant="primary"
            type="submit"
          >
            Зарегистроваться
          </Button>
        </div>
      </Form>
      {error && <p className="text-danger">{error}</p>}
    </Container>
  );
};

export default Registration;
