import './App.css';
import Header from './Components/Header';
import {
  Routes, Route, Link
} from "react-router-dom";
import LoginPage from './Pages/LoginPage';
import HomePage from './Pages/HomePage';



function App() {
  return (
    <>
     <div className="App">
        <Header></Header>
      </div>
   
     <Routes >
        <Route path='/' element={<HomePage/>}/>
        <Route path='/login' element={<LoginPage />} />
     </Routes>
     </>
  );
}

export default App;
