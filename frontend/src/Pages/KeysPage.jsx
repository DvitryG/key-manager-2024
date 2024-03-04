import React from 'react';
import SearchKeys from '../Components/SearchKeys';
import KeysCard from '../Components/KeysCard';

export const KeysPage = () => {
    return (
        <div>
            <div className="request-header p-4 ps-5">
                <h1>Выданные ключи</h1>
            </div>
        <SearchKeys/>
          <div className="container d-flex justify-content-center flex-column w-75">
          <KeysCard fullName="Ключ от" person="У: Иванова Ивана Ивановича"/>
          <KeysCard fullName="Ключ от" person="У: Иванова Ивана Ивановича"/>
          <KeysCard fullName="Ключ от" person="У: Иванова Ивана Ивановича"/>
          <KeysCard fullName="Ключ от" person="У: Иванова Ивана Ивановича"/>
          <KeysCard fullName="Ключ от" person="У: Иванова Ивана Ивановича"/>
          <KeysCard fullName="Ключ от" person="У: Иванова Ивана Ивановича"/>

          </div>
     
        </div>
    );
}
