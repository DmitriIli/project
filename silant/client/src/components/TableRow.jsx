import React, { useState } from 'react';
import Cell from './Cell';


const TableRow = (data) => {
    return (
        <div >
            {Object.keys(data.data).map((item)=>{
                return(
                    <>
                        {console.log(item)}
                    </>
                )
            })}
        </div>
    )
};

export default TableRow;