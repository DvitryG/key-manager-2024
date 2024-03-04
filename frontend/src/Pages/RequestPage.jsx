import React from 'react';
import Input from '../Components/Input';
import RequestForm from '../Components/RequestForm';

const RequestPage = () => {
    return (
        <div>
            <div className="request-header p-4 ps-5">
                <h1>Список Заявок</h1>
            </div>
          <RequestForm />
          
        </div>
    );
}

export default RequestPage;
