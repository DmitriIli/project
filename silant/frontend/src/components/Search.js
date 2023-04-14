import React from 'react'

export default function Search() {
    return (
        <div className='search'>
            <input className='input' type='text' placeholder='Заводской номер'/>
            <button className='buttonSubmit'>Поиск</button>
        </div>
    );
}
