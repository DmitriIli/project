import React from 'react'


export default function Table(props) {
{console.log(props.data[0])}
  return (
    <div>
      {props.data
        ?
        <div>
          
        </div>
        // <table>
        //   <thead>
        //     <tr key='head'>
        //       {props.data[0].verboseNames.map(item => {
        //         return <th className='th' key={item}>{item}</th>
        //       })}
        //     </tr>
        //   </thead>
        //   <tbody>
        //     {props.data[0].context.map(item => {
        //       return <tr key={item.factoryNumberMachine}>
        //         <td>{item.modelMachine}</td>
        //         <td>{item.factoryNumberMachine}</td>
        //         <td>{item.engine}</td>
        //       </tr>
        //     })}
        //   </tbody>
        // </table>
        :
        <div> Данные не загружены </div>
      }
    </div>
  )
}
