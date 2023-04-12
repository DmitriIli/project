import axios from "axios";
import React, { Component, Fragment, useState } from "react";
import { createRoot } from 'react-dom/client'
import Header from "./layout/Header";
import Search from "./layout/Search";
import DataService from "./DataService";


export default function App() {

  async function fetchData() {
    const data = await DataService.getAll();
    return data;
  }
  
  return (
    <div className="App" >
      <button onClick={fetchData}>onclick</button>
      <Search />
    </div>
  )
}

createRoot(document.getElementById('app')).render(<App />)


// {"context":[{"modelMachine":"ПД3,0","factoryNumberMachine":"0032","engine":"Kubota V3300","factoryNumberEngine":"2MU2983","transmission":"10VB-00106","factoryNumberTransmission":"21D0108251","driveAxel":"20VA-00101","factoryNumberDriveAxel":"21D0107997","steringAxel":"VS20-00001","factoryNumberSteringAxel":"21D0093265"},
// {"modelMachine":"ПД3,0","factoryNumberMachine":"0003","engine":"Kubota V3300","factoryNumberEngine":"2ME0639","transmission":"10VB-00106","factoryNumberTransmission":"21D0108264","driveAxel":"20VB-00102","factoryNumberDriveAxel":"21D0107988","steringAxel":"VS30-00001","factoryNumberSteringAxel":"0821004"}],
// "verboseNames":["Model Machine","Machine factory number","Engine","Engine Factory Number","Transmission","Transmission Factory Number","Drive Axel","Drive Axel Factory Number","Stering Axel","Stering Axel Factory Number"]}