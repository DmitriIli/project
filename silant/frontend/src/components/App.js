import React, { useEffect } from 'react'
import { useDispatch, useSelector } from "react-redux";
import DataService from "./DataService"
import Search from "./layout/Search";
import Table from "./layout/Table";

export default function App() {

  const dispatch = useDispatch()
  const machines = useSelector(state => state.machines.machines)

  async function fetchData() {
    const responce = await DataService.getAll()
    dispatch({ type: "GETMACHINES", payload: responce })
  }

 
  return (
    <div className="App" >
      <Search />
      <button className='button' onClick={fetchData}>get data</button>
      <Table data={machines} />
    </div>
  )
}