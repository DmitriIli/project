import React from 'react'


export default function Table(props) {
  { console.log( typeof(props.data[0])) }
  return (
    <div>
      {props.data[0]
        ?
        <div>

          <table>
            <thead>
              <tr key='head'>
                {props.data[0].verboseNames.map(item => {
                  return <th className='th' key={item}>{item}</th>
                })}
              </tr>
            </thead>
            <tbody>
              {props.data[0].context.map(item => {
                return <tr key={item.factoryNumberMachine}>
                  {
                    Object.keys(props.data[0].context[0]).map(name => {
                      return <td key={name+item[name]}>{item[name]}</td>
                    })
                  }
                </tr>
              })}
            </tbody>
          </table>
        </div>
        :
        <div> Данные не загружены </div>
      }
    </div>
  )
}
