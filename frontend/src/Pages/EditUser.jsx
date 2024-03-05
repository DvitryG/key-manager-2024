import React from "react";
import Editing from "../Components/Editing";
import '../Styles/editUser.css'

function  EditUser(){
    return (
        <>
            <div className="header">
                <h1>Редактировать пользователя</h1>
            </div>
            <Editing/>
        </>
    );
}

export default EditUser;
