import './App.css';
import Header from './Components/Header';
import {
  Routes, Route
} from "react-router-dom";
import LoginPage from './Pages/LoginPage';
import ProfilePage from './Pages/ProfilePage';
import RegistrationPage from './Pages/RegistrationPage';
import RequestPage from './Pages/RequestPage';
import KeysPage  from './Pages/KeysPage';
import UserListPage from './Pages/UserListPage';
import OfficesPage from './Pages/OfficesPage';
import EditUser from './Pages/EditUser';
import NoAuth from './Pages/NoAuth';
import Logout from './Pages/Logout';
import ConfirmReturn from './Pages/ConfirmReturn'



function App() {
  return (
    <>
     <div className="App">
        <Header></Header>
      </div>
   
     <Routes >
        <Route path='/login' element={<LoginPage />} />
        <Route path='/registration' element={<RegistrationPage />} />
        <Route path='/requests'  element={<RequestPage />}/>
        <Route path='/keys'  element={<KeysPage />}/>
        <Route path='/list' element={<UserListPage />}/>
        <Route path='/office' element={<OfficesPage />}/>
        <Route path='/profile' element={<ProfilePage/>}/>
        <Route path='/users' element={<EditUser/>}/>
        <Route path='/noauth' element={<NoAuth/>}/>
        <Route path='/logout' element={<Logout/>}/>
        <Route path='/confirm_return' element={<ConfirmReturn/>} />


     </Routes>
     </>
  );
}

export default App;
