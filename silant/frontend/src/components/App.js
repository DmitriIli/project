import React, { useEffect } from 'react'
import { useDispatch, useSelector } from "react-redux";
import DataService from "./DataService"
import Search from "./Search";
import Table from "./Table";
import Header from './Header';

export default function App() {

  const dispatch = useDispatch()
  const machines = useSelector(state => state.machines.machines)

  async function fetchData() {
    const responce = await DataService.getAll()
    dispatch({ type: "GETMACHINES", payload: responce })
  }

  useEffect(() => {
    fetchData()
  }, [])


  return (
    <div className="App" >
      <Search />
      <Header data={machines} />
      <Table data={machines} />
    </div>
  )
}