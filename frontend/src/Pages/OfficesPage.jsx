import React from 'react';
import CardOffices from '../Components/CardOffices';
import SearchOffices from '../Components/SearchOffices';
import ListOffices from '../Components/ListOffices';
const data = [
    {
        "id": 1,
        "room": 200,
        "available": true,
    },
    {
        "id": 2,
        "room": 203,
        "available": false,
    },
    {
        "id": 3,
        "room": 304,
        "available": false,
    },
    {
        "id": 4,
        "room": 404,
        "available": false,
    },
    {
        "id": 5,
        "room": 300,
        "available": true,
    },
];
const renderOffice = data.map((office)=>
    <ListOffices key={office.id} room={office.room} available={office.available}/>   
);
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
                  {renderOffice}
          </div>
     
        </div>
    );
}

export default OfficesPage;