import React, { useState } from 'react';
import Cell from './Cell';


const TableRow = (props) => {
    return (
        <div className='table-row'>
            {Object.keys(props.data).map((item)=>{
                return(
                    <>
                        <Cell data={props.data[item]} key={props.data[item]+Date.now()} />
                    </>
                )
            })}
        </div>
    )
};

export default TableRow;