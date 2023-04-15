import React from 'react'

export default function Header(props) {
  { console.log(props.data[0]) }
  return (
    <div>
      {props.data[0]
        ?
        <div className="table__row--header">{props.data[0].verboseNames.map(item => {
          return <div key={item}>{item}</div>
        })}</div>
        :
        <div> Данные не загружены </div>
      }
    </div>
  )
}
