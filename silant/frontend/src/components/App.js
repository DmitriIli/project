import React, { useState, useEffect } from 'react';
import { render } from "react-dom";



function App() {

  const [dataJoined, setDataJoined] = useState('')
  const [error, setError] = useState()

  useEffect(() => {
    fetch('/api/get/')
      .then(response => {
        if (response.ok) {
          return response.json()
        } else {
          throw Error(`Something went wrong: code ${response.status}`)
        }
      })
      .then(({ data }) => {
        setDataJoined(data)
      })
      .catch(error => {
        console.log(error)
        setError('Ошибка, подробности в консоли')
      })
  }, [])

  return (
    <div className="App">
      
    </div>
  );

}
export default App;

const container = document.getElementById("app");
render(<App />, container);
