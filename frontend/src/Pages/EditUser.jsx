import React, { useState } from 'react';
import axios from 'axios';
import {url} from "../url.js";
function Editing({ user_id }) {
    const [roles, setRoles] = useState({
        include: [],
        exclude: [],
    });
    const [error, setError] = useState("");

    const handleCheckboxChange = (event) => {
        const { name, checked } = event.target;
        if (checked) {
            setRoles(prevState => ({
                ...prevState,
                include: Array.from(new Set([...prevState.include, name])),
                exclude: prevState.exclude.filter(item => item !== name),
            }));
        } else if (!checked && roles.include.includes(name)) {
            setRoles(prevState => ({
                ...prevState,
                include: prevState.include.filter(item => item !== name),
                exclude: Array.from(new Set([...prevState.exclude, name])),
            }));
        } else if (!checked && roles.exclude.includes(name)) {
            setRoles(prevState => ({
                ...prevState,
                include: Array.from(new Set([...prevState.include, name])),
                exclude: prevState.exclude.filter(item => item !== name),
            }));
        }
    };
    
    
        

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            await axios.put(`${url}/users/${user_id}`, {
                include: roles.include,
                exclude: roles.exclude,
            });
            // Handle success
        } catch (error) {
            console.error('Error updating user:', error);
            setError("Problem editing user. Please try again.");
        }
    };

    return (
        <div className="container d-flex justify-content-center align-items-center">
            <div className="form mt-5">
                {error && <p className="text-danger">{error}</p>}
                <form onSubmit={handleSubmit}>
                    <label className="label_blo">Роли</label>
                    <div className="d-flex flex-column align-items-center">
                        <label htmlFor="student" className="check mb-2">
                            <input type="checkbox" id="student" name="student" onChange={handleCheckboxChange} />
                            Студент
                        </label>
                        <label htmlFor="teacher" className="check mb-2">
                            <input type="checkbox" id="teacher" name="teacher" onChange={handleCheckboxChange} />
                            Преподаватель
                        </label>
                        <label htmlFor="dean" className="check mb-2">
                            <input type="checkbox" id="dean" name="dean" onChange={handleCheckboxChange} />
                            Деканат
                        </label>
                        <label htmlFor="admin" className="check mb-2">
                            <input type="checkbox" id="admin" name="admin" onChange={handleCheckboxChange} />
                            Админ
                        </label>
                    </div>
                    <input type="submit" value="Изменить" onClick={handleCheckboxChange} className="btn btn-primary mt-3" />
                </form>
            </div>
        </div>
    );
}

export default Editing;
