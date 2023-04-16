import React from 'react';

export default function HeaderRows(props) {

    return (
        <>
            {props.data
                ?
                props.data.map((item) => {
                    return <div key={item} className='rows-item'>{item}</div>
                })
                : <div></div>
            }
        </>
    )
}
