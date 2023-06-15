import React from 'react'
import TableRow from './TableRow';
import TitleRow from './TitleRow';


export default function Table(props) {
    return (
        <div>
            <div className='table-header'>
                <TitleRow data={props.titles} />
            </div>
            <div className='table-body'>
                {props.data.map((row) => {
                    return (
                        <>
                            <TableRow data={row} />
                        </>
                    )
                })}
            </div>
        </div>
    )
}
