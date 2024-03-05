import React from 'react';


import "../Styles/styleYusuf.css";


const Profile = () => {
    return (
        <>
        <form>
            <div className='login'>
                <div className='form-group'>
                    <h6 className="textTitle">ФИО</h6>
                    <input className="inputText" type="text" placeholder='Иванов Иван Иванович' />
                    <h6 className="textTitle">Email</h6>
                    <input className="inputText" type="email" placeholder='example@gmail.com' />
                    <button className='btn btn-search'>Сохранить Изменение</button>
                </div>
            </div>
        </form>

        <div className="form-group">
            <form className="login">
                <h6 className="textTitle">Старый пароль</h6>
                <input className="inputText" type="password" placeholder='Введите пароль' />
                <h6 className="textTitle">Новый пароль</h6>
                <input className="inputText" type="password" placeholder='Повторите пароль'/>
                <button className='btn btn-search'>Сменить пароль</button>
            </form>
        </div>
       </>
        
    );
};

export default Profile;