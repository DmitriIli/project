import axios from "axios";
import React, { Component, Fragment, useState } from "react";
import { createRoot } from 'react-dom/client'
import Header from "./layout/Header";
import Search from "./layout/Search";
import DataService from "./DataService";


export default function App() {

  async function fetchData(){
    const data = await DataService.getAll();    
    return data;
  }

  // const [machines, setMachines] = useState();
  const [[value, setValue]] = useState();
  
  return (
    <div className="App" >
      <Search />
    </div>
  )
}

createRoot(document.getElementById('app')).render(<App />)
