import React from 'react';
import RequestForm from '../Components/RequestForm';
import Card from '../Components/Card';

const RequestPage = () => {
    return (
        <div>
            <div className="request-header p-4 ps-5">
                <h1>Список заявок</h1>
            </div>
          <RequestForm />
          <div className="container d-flex justify-content-center flex-column w-75">
          <Card fullName="name" room="203" date="mn 10:35-12:10" status="bad"/>
          <Card fullName="name" room="201" date="st 10:35-12:10" status="good"/>
          </div>
     
        </div>
    );
}

export default RequestPage;

