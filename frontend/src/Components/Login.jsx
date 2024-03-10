import React, {useState} from "react";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import "../Styles/index.css";
import "../Styles/button.css";
import "../Styles/styleYusuf.css";
import { Link } from "react-router-dom";
import axios from "axios";



const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post(
        "http://0.0.0.0:5000/users/login",
        {
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
      // Login successful
      console.log("Login successful:", response.data);
      // Assuming the response contains an access token
      const { access_token } = response.data;
      // Store the access token in local storage or state for further use
      localStorage.setItem("accessToken", access_token);
      // Optionally, you can redirect the user to another page after successful login
    } catch (error) {
      // Handle login failure
      console.error("Login error:", error);
      setError("Invalid email or password. Please try again.");
    }
  };
  return (<Container className="mt-3 w-50">
  <Form className="reg" onSubmit={handleSubmit}>
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
        placeholder="Password"
        value={password}
        onChange={handlePasswordChange}
      />
    </Form.Group>
    <div>
      <Button
        className="logbtn d-grid gap-2 col-6 mx-auto"
        variant="secondary"
        type="submit"
      >
        Войти
      </Button>
      <Button className="regbtn d-grid gap-2 col-6 mx-auto" variant="primary">
        <Link to="/registration">Регистрация</Link>
      </Button>
    </div>
  </Form>
  {error && <p className="text-danger">{error}</p>}
</Container>
  );
};

export default Login;
