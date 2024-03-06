import React from 'react';
import CardOffices from '../Components/CardOffices';
import SearchOffices from '../Components/SearchOffices';
import ListOffices from '../Components/ListOffices';

function OfficesPage(){
    return (
        <div>
            <div className="request-header p-4 ps-5">
                <h1>Список кабинетов</h1>
            </div>
            <div className='d-flex flex-row justify-content-center'>
            <CardOffices />
             <SearchOffices/>
            </div>

             <div className="container d-flex justify-content-center flex-column w-75">
                  <ListOffices room="Кабинет ХХХ"/>
                     <ListOffices room="Кабинет ХХХ"/>
                     <ListOffices room="Кабинет ХХХ"/>
                     <ListOffices room="Кабинет ХХХ"/>
                     <ListOffices room="Кабинет ХХХ"/>
          </div>
     
        </div>
    );
}

export default OfficesPage;