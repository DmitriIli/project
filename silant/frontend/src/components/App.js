import React, { useEffect, useState, useMemo } from 'react'
import { useDispatch, useSelector } from "react-redux";
import DataService from "./DataService"
import Search from "./Search";
import Machines from './Machines';
import Sorted from './Sorted';
import Button from './Button';

export default function App() {


  const dispatch = useDispatch()
  const machines = useSelector(state => state.machines.machines)
  const verboseNames = useSelector(state => state.machines.verboseNames)
  const [searchData, setSearchData] = useState('')
  const [selectData, setSelectData] = useState('modelMachine')



  async function fetchData() {
    const responce = await DataService.getAll()
    dispatch({ type: "GETMACHINES", payload: responce })
  }

  useEffect(() => {
    fetchData()
  }, [])

  const selectedData = (sort) => {
    setSelectData(sort)
    console.log(selectData)
  }

  const addSearchData = (e) => {
    e.preventDefault()
    console.log(searchData)
  }

  const sortedList = useMemo(() => {
    if (selectData) {
      let arr = [...machines]
      return arr.sort((a, b) => { a[selectData].localeCompare(b[selectData]) })
    } else {

      return machines
    }
  }, [selectData])

  const sortedAndSearchList = useMemo(()=>{
    if (sortedList[0]){
      return sortedList[0].filter(item=>item['modelMachine'].includes(searchData))
    }
    
  }, [searchData,sortedList])



  return (
    <div className="App" >
      <div className='search-sorted-block'>
        <Search
          value={searchData}
          onChange={e => setSearchData(e.target.value)}
          type='text'
          placeholder='модель машины'

        />
        <Button onClick={addSearchData}> Поиск </Button>
        <Sorted
          value={selectData}
          onChange={selectedData}
          defaultValue='Сортировка по...'
          options={[
            { value: 'modelMachine', name: 'Модель техники' },
            { value: 'engine', name: 'Модель двигателя' },
            { value: 'transmission', name: 'Модель трансмисси' },
            { value: 'driveAxel', name: 'Модель управляемого моста' },
            { value: 'steringAxel', name: 'Модель ведущего моста' },
          ]}
        />
      </div>

      <Machines machines={sortedList} verboseNames={verboseNames} />
    </div>
  )
}