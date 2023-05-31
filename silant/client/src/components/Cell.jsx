import React, { useState } from 'react';

const TableCell = ({ props }) => {
  const [state, setState] = useState(props.item);

  return (
    <div className="table__cell">
      <input
        value={state}
        onChange={({ target }) => setState(target.value)}
        type="text" />
    </div>
  )
}

export default TableCell;