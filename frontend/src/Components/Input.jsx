import React from 'react';

const Input = ({title, placeholder}) => {
    return (
        <div className='mb-2 me-4'>
            <div className='input-title mb-1'>{title}</div>
            <input type="text" placeholder={placeholder} className='input form-control'></input>
        </div>
    );
}

export default Input;
