import React, { useState } from 'react';

const Cell = (props) => {
  const [state, setState] = useState(props.data);

  return (
    <div className="table-cell">
      {/* < input
        value={state}
        onChange={({ target }) => setState(target.value)}
        type="text" /> */}
      <>{state}</>
    </div>
  )
}
export default Cell;