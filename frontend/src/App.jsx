import './App.css';
import Header from './Components/Header';
import {
  Routes, Route
} from "react-router-dom";
import LoginPage from './Pages/LoginPage';
import HomePage from './Pages/HomePage';
import RegistrationPage from './Pages/RegistrationPage';
import RequestPage from './Pages/RequestPage';
import {KeysPage}  from './Pages/KeysPage';



function App() {
  return (
    <>
     <div className="App">
        <Header></Header>
      </div>
   
     <Routes >
        <Route path='/' element={<HomePage/>}/>
        <Route path='/login' element={<LoginPage />} />
        <Route path='/registration' element={<RegistrationPage />} />
        <Route path='/requests'  element={<RequestPage />}/>
        <Route path='/keys'  element={<KeysPage />}/>
     </Routes>
     </>
  );
}

export default App;
