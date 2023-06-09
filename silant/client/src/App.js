import { useState, useEffect, useMemo } from 'react';
import './styles/App.css';
import InputComponent from './components/ui/input/InputComponent';
import ButtonComponent from './components/ui/button/ButtonComponent';
import SelectedComponent from './components/ui/select/SelectedComponents';
import Table from './components/Table';
import axios from 'axios';

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}


function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(true)
  const [loading, setLoading] = useState()
  const [authForm, setAuthForm] = useState({ username: '', password: '' })
  const [userData, setUserData] = useState({ firstName: '', lastName: '', userName: '', email: '', dateJoined: '' })
  const [data, setData] = useState()
  const [sortedData, setSortedData] = useState()
  const [selectedSort, setSelectedSort] = useState('earlier')
  const [searchQuery, setSearchQuery] = useState('')
  const [titles, setTitles] = useState()
  const [error, setError] = useState()
  const [user, setUser] = useState()
  const csrftoken = getCookie('csrftoken')


  useEffect(() => {
    fetch(
      '/api/get/',
      {
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
        },
      }
    ).then(response => {
      if (response.ok) {
        return response.json()
      } else {
        throw Error(`Something went wrong: code ${response.status}`)
      }
    }
    ).then(({ data }) => {
      setData(data.data)
      setTitles(data.titles)
      setError(null)

    }
    ).catch(error => {
      console.log(error)
      setError('Ошибка, подробности в консоли')
      setIsLoggedIn(false)
    }
    )
  }, [isLoggedIn])

  useEffect(() => {
    if (isLoggedIn) {
      fetch(
        '/api/user/',
        {
          headers: {
            'Content-Type': 'application/json;charset=utf-8',
          },
        }
      )
        .then(response => {
          if (response.ok) {
            return response.json()
          } else {
            throw Error(`Something went wrong: code ${response.status}`)
          }
        })
        .then(({ data }) => {
          setUserData({ firstName: data.first_name, lastName: data.last_name, username: data.username, email: data.email, dateJoined: data.date_joined })
          setError(null)
        })
        .catch(error => {
          console.log(error)
          setError('Ошибка, подробности в консоли')
          setIsLoggedIn(false)
          setUser('')
        })
    }
  }, [isLoggedIn])

  const logoutHandler = e => {

    fetch('api/logout/',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
          'X-CSRFToken': csrftoken,
        },
      }
    ).then(() => fetch('/api/get/',
      {
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
        },
      }
    ).then(response => {
      if (response.ok) {
        return response.json()
      } else {
        throw Error(`Something went wrong: code ${response.status}`)
      }
    }
    ).then(({ data }) => {
      setData(data.data)
      setTitles(data.titles)
      setError(null)
    }
    ).catch(error => {
      console.log(error)
      setError('Ошибка, подробности в консоли')
      setUser('')
    }))
    setIsLoggedIn(false)
    setAuthForm({ userName: '', password: '' })
  }

  const submitHandler = e => {
    e.preventDefault();
    setLoading(true);
    fetch(
      '/api/login/',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
          username: authForm.username,
          password: authForm.password,
        })
      }
    )
      .then(response => {
        if (response.ok) {
          return response.json()
        } else {
          throw Error(`Something went wrong: code ${response.status}`)
        }
      })
      .then((responce) => {
        setIsLoggedIn(true)
        setError(null)
        setUser(responce.user)
      })
      .catch(error => {
        console.log(error)
        setError('Ошибка, подробности в консоли')
      })
      .finally(setLoading(false))
  }

  const sortData = (sort) => {
    setSelectedSort(sort)
    if (isLoggedIn) {
      if (sort === 'earlier') {
        setData([...data].sort((a, b) => a['shipingDate'].localeCompare(b['shipingDate'])))
      }
      if (sort === 'later') {
        setData([...data].sort((a, b) => b['shipingDate'].localeCompare(a['shipingDate'])))
      }
    }
    else {
      setSortedData([...data])
    }
  }


  const searchedData = useMemo(() => {
    if (data) {
      if (searchQuery) { console.log(([...data].filter(item => item.factoryNumberMachine.includes(searchQuery)))) }
      // return [...data]
      return null
    }
    return null
  }, [searchQuery, data])


  async function getData() {
    const responce = await axios.get('http://localhost:3000/api/get');
    // const responce = await axios.get('http://localhost:3000/api/get', {
    //   withCredentials: false,
    // }).then(responce => {
    //   console.log(responce.headers['set-cookie']);
    // }).catch(e => {
    //   console.log(e)
    // })
    console.log(responce)
    return responce
  }

  return (
    <div className="App">
      <div className="header">
        <div className='header-content'>
          <div className="logo">
            <a href="/">
              <img src="logo.svg" width="60" height="60px" alt='logo' />
            </a>
          </div>
          {!isLoggedIn
            ? loading ? "Загрузка..." :
              <form className='auth-form' onSubmit={submitHandler}>
                <InputComponent name="username" placeholder="username" type="text" value={authForm.username} onChange={e => setAuthForm({ ...authForm, username: e.target.value })} />
                <InputComponent name="password" placeholder="password" type="password" value={authForm.password} onChange={e => setAuthForm({ ...authForm, password: e.target.value })} />
                <ButtonComponent>Войти</ButtonComponent>
              </form>
            : !error ?
              <div>
                <h3>{userData.username}</h3>
                <ButtonComponent className="button" onClick={logoutHandler}> Выйти </ButtonComponent>
              </div>
              : null
          }</div>
      </div>
      {error ? <p>{error}</p> : null}

      {data
        ?
        <div className='body'>
          <div className='sort-menu'>
            <hr />
            {isLoggedIn
              ? <SelectedComponent
                value={selectedSort}
                onChange={sortData}
                defaultValue="Сортировка по дате..."
                options={[
                  { value: 'earlier', name: 'По возрастанию' },
                  { value: 'later', name: 'По убыванию' },
                ]}
              /> : null}
            <InputComponent
              placeholder="Заводской номер машины..."
              type="text"
              value={searchQuery}
              onChange={e => setSearchQuery(e.target.value)}
            />
            <hr />
          </div>
          <button onClick={getData}>get</button>
          <div className='table'>
            <Table titles={titles} data={data} />
          </div>
        </div>
        : <h1>данные не загружены</h1>
      }
    </div>
  )
};
export default App;