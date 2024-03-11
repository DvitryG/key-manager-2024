import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CardOffices from '../Components/CardOffices';
import SearchOffices from '../Components/SearchOffices';
import ListOffices from '../Components/ListOffices';
import {url} from "../url.js";
function OfficesPage() {
    const [offices, setOffices] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchOffices = async () => {
            try {
                const accessToken = localStorage.getItem('accessToken');
                const response = await axios.get(`${url}/rooms/?page=0&page_size=10`, {
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                        'accept': 'application/json'
                    }
                });
                setOffices(response.data.rooms);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching offices:', error);
                setError('Error fetching offices. Please try again.');
                setLoading(false);
            }
        };

        fetchOffices();
    }, []);

    return (
        <div>
            <div className="request-header p-4 ps-5">
                <h1>Список кабинетов</h1>
            </div>
            <div className='d-flex flex-row justify-content-center'>
                <CardOffices />
                <SearchOffices />
            </div>
            <div className="container d-flex justify-content-center flex-column w-75">
                {loading ? (
                    <p>Loading...</p>
                ) : error ? (
                    <p>{error}</p>
                ) : (
                    offices.map(office => (
                        <ListOffices key={office.room_id} name={office.name} room_id={office.room_id} blocked={office.blocked} />
                    ))
                )}
            </div>
        </div>
    );
}

export default OfficesPage;
