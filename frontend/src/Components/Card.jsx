import React, {useEffect, useState} from 'react';
import "../Styles/index.css";
import '../Styles/button.css';
import axios from "axios";
import {url} from "../url";

const CardComponent = ({ fullName, room, date, status, order_id }) => {
    const [order, setOrder] = useState([]);
    useEffect(() => {
        setOrder(order_id);
    }, []);

    const handleClose = async(event) =>{
        event.preventDefault();
        try {
            const accessToken = localStorage.getItem('accessToken');
            const response = await axios.put(`${url}/orders/${order}/close`, {
                headers: {
                    'Authorization': `Bearer ${accessToken}`,
                    'accept': 'application/json'
                }
            });
        } catch (error) {
            console.error('Error close order:', error);
        }
    }
    const handleApprove = async(event) =>{
        event.preventDefault();
        try {
            const accessToken = localStorage.getItem('accessToken');
            const response = await axios.put(`${url}/orders/${order}/approve`, {
                headers: {
                    'Authorization': `Bearer ${accessToken}`,
                    'accept': 'application/json'
                }
            });
        } catch (error) {
            console.error('Error approve order:', error);
        }
    }
    return (
        <>
        <div className='d-flex justify-content-between mb-2 line'>
            <div className='d-flex flex-column'>
                <div className='mb-2 fw-semibold'>{fullName} </div>
                <div>Кабинет: {room} | {date}</div>
            </div>
            <div className='d-flex flex-row p-2'>
                {status == 'opened' ? (
                    <>
                        <div className='btn btn-done me-2' onClick={handleApprove}>Одобрить</div>
                        <div className='btn btn-outline-danger' onClick={handleClose}>Закрыть</div>
                    </> )
                   : status == 'approved' ? ( <>
                  <div className='btn btn-outline-danger' onClick={handleClose}>Закрыть</div>
                  </> ) : <></>
                  }

            
              
            </div>
        </div>
       </>
        
    );
};

export default CardComponent;