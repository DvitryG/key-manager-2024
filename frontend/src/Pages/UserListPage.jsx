import React from 'react';
import UserSearch from '../Components/UserSearch';
import UserList from '../Components/UserList';


export const UserListPage = () => {
    return (
        <div>
            <div className="request-header p-4 ps-5">
                <h1>Список пользователей</h1>
            </div>
         <UserSearch/> 
          <div className="container d-flex justify-content-center flex-column w-75">
          <UserList fullName="Иванов Иван Иванович" email="name@example.com" status="студент, преподаватель"/>
          <UserList fullName="Иванов Иван Иванович" email="name@example.com" status="преподаватель"/>
          <UserList fullName="Иванов Иван Иванович" email="name@example.com" status="студент, преподаватель"/>
          <UserList fullName="Иванов Иван Иванович" email="name@example.com" status="деканат"/>
          <UserList fullName="Иванов Иван Иванович" email="name@example.com" status="преподаватель"/>
          <UserList fullName="Иванов Иван Иванович" email="name@example.com" status="админ"/>

          </div>
     
     </div>
    );
}
