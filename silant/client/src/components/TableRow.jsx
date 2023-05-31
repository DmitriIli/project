import React, { useState } from 'react';

const TableRow = ({starship}) => {
    const {
      cargo_capacity,
      cost_in_credits,
      max_atmosphering_speed,
      name
    } = starship
  
  
    return (
      <div className="table__row">
        <TableCell item={cargo_capacity} />
      </div>
    )
  };

  export default TableRow;