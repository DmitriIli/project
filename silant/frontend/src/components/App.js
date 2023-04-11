import React, { useState, useEffect } from 'react';
import { render } from "react-dom";
import Search from './UI/Search';


function App() {

  const [dataJoined, setDataJoined] = useState('')
  const [error, setError] = useState()

  const [value, setValue] = useState()

  useEffect(() => {
    fetch('api/index/')
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
      <Search />
    </div>
  );

}
export default App;

const container = document.getElementById("app");
render(<App />, container);
