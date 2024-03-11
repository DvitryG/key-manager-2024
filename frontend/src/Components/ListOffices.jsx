import React from 'react';
import axios from 'axios';

function ListOffices({ id, name, available }) {
  const deactivateOffice = async () => {
    try {
      await axios.post(`  'http://0.0.0.0:5000/rooms/${id}?availability=false' \
      `);
      // Handle success or update UI as needed
    } catch (error) {
      console.error('Error deactivating office:', error);
      // Handle error or show error message
    }
  };

  const activateOffice = async () => {
    try {
      await axios.post(`http://0.0.0.0:5000/rooms/${id}?availability=true`);
      // Handle success or update UI as needed
    } catch (error) {
      console.error('Error activating office:', error);
      // Handle error or show error message
    }
  };

  const deleteOffice = async () => {
    try {
      await axios.delete(`http://0.0.0.0:5000/rooms/${id}`);
      // Handle success or update UI as needed
    } catch (error) {
      console.error('Error deleting office:', error);
      // Handle error or show error message
    }
  };

  return (
    <>
      <div className='d-flex justify-content-between mb-2 line'>
        <div className='d-flex flex-column'>
          <div className='d-flex w-50 justify-content-start'>Кабинет: {name}</div>
        </div>
        {available ? (
          <button className='btn btn-good mb-3 w-25' onClick={deactivateOffice}>Сделать недоступным</button>
        ) : (
          <button className='btn btn-good mb-3 w-25' onClick={activateOffice}>Сделать доступным</button>
        )}
        <button className='btn btn-bad mb-3 w-25' onClick={deleteOffice}>Удалить</button>
      </div>
    </>
  );
}

export default ListOffices;
