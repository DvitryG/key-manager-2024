import './App.css';
import Header from './Components/Header';
import {
  Routes, Route
} from "react-router-dom";
import LoginPage from './Pages/LoginPage';
import HomePage from './Pages/HomePage';
import ProfilePage from './Pages/ProfilePage';
import RegistrationPage from './Pages/RegistrationPage';
import RequestPage from './Pages/RequestPage';
import {KeysPage}  from './Pages/KeysPage';
import {UserListPage} from './Pages/UserListPage';


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
        <Route path='/list' element={<UserListPage />}/>
        <Route path='/profile' element={<ProfilePage/>}/>
     </Routes>
     </>
  );
}

export default App;
