import React from 'react'
import ContentRows from './ContentRows'
import HeaderRows from './HeaderRows'

export default function Machines(props) {

    return (
        <div className='machines-table'>
            <div className='machines-list'>
                <div className='rows-header'>
                    <HeaderRows data={props.verboseNames[0]} />
                </div>
                <div className='rows-context'>
                    <ContentRows data={props.machines[0]} />
                </div>
            </div>
        </div>
    )
}
