import React, { useState } from 'react';
import Cell from './Cell';

const TitleRow = (data) => {
    return (
        <div className="table-row">
           { data.data.map(item => 
                <Cell data={item} key={item} />
            )}
        </div>
    )
};

export default TitleRow;