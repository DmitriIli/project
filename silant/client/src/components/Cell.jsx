import React, { useState } from 'react';

const Cell = (props) => {
  const [state, setState] = useState(props.data);

  return (
    <div className="table__cell">
      {/* {/* <input
        value={state}
        onChange={({ target }) => setState(target.value)}
        type="text" /> */}
        <p>{state}</p> */
        {console.log(props.data)}
    </div>
  )
}

export default Cell;