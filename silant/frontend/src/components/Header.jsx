import React from 'react'

export default function Header(props) {
  { console.log(props.data[0]) }
  return (
    <div>
      {props.data[0]
        ?
        <div>{props.data[0].verboseNames.map(item => {
          return <div>{item}</div>
        })}</div>
        :
        <div> Данные не загружены </div>
      }
    </div>
  )
}
