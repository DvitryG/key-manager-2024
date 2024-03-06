import React from 'react';
import RequestForm from '../Components/RequestForm';
import Card from '../Components/Card';

const data = [
    {
        "id": 1,
        "name": "Имя",
        'date': "8:00-10:00",
        "status": 1,
        "room": 250,
    },
    {
        "id": 2,
        "name": "Имя Фамилия ",
        'date': "18:00-20:00",
        "status": 2,
        "room": 201,
    },
    {
        "id": 1,
        "name": "Фио",
        'date': "12:00-14:00",
        "status": 2,
        "room": 202,
    },
    {
        "id": 1,
        "name": "Name",
        'date': "8:00-10:00",
        "status": 0,
        "room": 400,
    }
];
const renderRequests = data.map((request)=>
    <Card fullName={request.name} room={request.room} date={request.date} status={request.status}/>
);

const RequestPage = () => {
    return (
        <div>
            <div className="request-header p-4 ps-5">
                <h1>Список заявок</h1>
            </div>
          <RequestForm />
          <div className="container d-flex justify-content-center flex-column w-75">
            {renderRequests}
          </div>
     
        </div>
    );
}

export default RequestPage;

