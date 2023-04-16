import React, { Component } from 'react'

export default function Sorted({ options, defaultValue, value, onChange }) {

    return (
        <select
            value={value}
            onChange={event => onChange(event.target.value)}
        >
            <option disabled value=''>{defaultValue}</option>
            {
                options.map((option) => {
                    return <option value={option.value} key={option.value}>
                        {option.name}
                    </option>
                })
            }
        </select>
    )
}
