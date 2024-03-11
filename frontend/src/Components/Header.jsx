import React, {useState, useEffect} from 'react';
import "../index.css";
import "../App.css";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom';
import '../Styles/index.css'


const Header = () => {
    const [auth, setAuth] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem('accessToken');
        if (token != null){
            setAuth(true);
        }
    }, []);
    useEffect(() => {
        const token = localStorage.getItem('accessToken');
        if (token != null){
            setAuth(true);
        }
    }, [auth]);
    useEffect(() => {
        const token = localStorage.getItem('accessToken');
        if (token == null){
            setAuth(false);
        }
    }, [auth]);
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
                <Link to="/keys" className='me-2'>Выданные ключи</Link>

                <Link to="/confirm_return" className='me-2'>Выданные ключи</Link>
              </Nav>
              <Nav>
              <Nav>


                  {auth ? (<>
                      <Link to="/profile" className='me-2'>Профиль</Link>
                      <Link to="/users" className='me-2'>Редактировать пользователя</Link>
                      <Link to="/logout" className='me-2'>выход из системы</Link>
                  </>) : (<>
                      <Link to="/login" className='me-2'>Войти</Link>
                      <Link to="/registration" className='me-2'>Регистрация</Link>
                  </>)}

               </Nav>
              </Nav>
            </Container>
          </Navbar>
      );
}

export default Header;
