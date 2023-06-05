import React, { useState } from 'react';
import Cell from './Cell';

const TableRow = (data) => {
    return (
        <div className="table__row">
            {data.data.map(item => {
                <Cell data={item} key={item} />
            })
            }
        </div>
    )
};

export default TableRow;