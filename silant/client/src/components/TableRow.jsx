import React, { useState } from 'react';
import Cell from './Cell';

// let keys = Object.keys(i)

const TableRow = (data) => {
    return (
        <div className="table-row">
            {
                // data.map(item =>
                //     <Cell data={item} key={item} />
                // )
                Object.keys(data).map = (keyItem) => {
                    <Cell data={data[keyItem]} key={data[keyItem] + keyItem} />
                }
            }
        </div>
    )
};

export default TableRow;