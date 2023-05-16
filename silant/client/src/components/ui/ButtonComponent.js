import React from 'react'

const ButtonComponent = ({children, ...props}) => {
  return (
    <button {...props} className='button'>
        {children}
    </button>
  )
}

export default ButtonComponent