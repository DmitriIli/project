import React from 'react';

export default function ContentRows(props) {

    return (
        <>
            {props.data
                ?
                props.data.map((machine) => {
                    return <div key={machine['factoryNumberMachine']} className='rows-item'>
                        {
                            Object.keys(props.data[0]).map((prop) => {
                                return <div key={prop + machine[prop]} className='rows-item'>{machine[prop]}</div>
                            })
                        }
                    </div>
                })
                : <div></div>
            }
        </>
    )
}
