import React from 'react';
import CardOffices from '../Components/CardOffices';
import SearchOffices from '../Components/SearchOffices';

const OfficesPage = () => {
    return (
        <div>
            <div className="request-header p-4 ps-5">
                <h1>Список кабинетов</h1>
            </div>
            <div className='d-flex flex-row justify-content-center'>
            <CardOffices />
          <SearchOffices/>
            </div>
          
          {/* <div className="container d-flex justify-content-center flex-column w-75">
          <Card fullName="name" room="203" date="mn 10:35-12:10" status="bad"/>
          <Card fullName="name" room="201" date="st 10:35-12:10" status="good"/>
          </div> */}
     
        </div>
    );
}

export default OfficesPage;