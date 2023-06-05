import { useState, useEffect } from 'react';
import './styles/App.css';
import InputComponent from './components/ui/InputComponent';
import ButtonComponent from './components/ui/ButtonComponent';
import TableRow from './components/TableRow';


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
  const [error, setError] = useState()
  const [gettDataError, setGetDataError] = useState()
  const [authError, setAuthError] = useState()
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
      setData(data)
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
          console.log(data)
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
      setData(data)
      setError(null)
    }
    ).catch(error => {
      console.log(error)
      setError('Ошибка, подробности в консоли')
      setUser('')
    }))
    // setUser('')
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
  return (
    <div className="App">
      <div className="header">
        <div className='header-content'>
          <div class="logo">
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
        <div className='table-header'>
          {/* {data.titles.map((item) =>
            <h3>{item}</h3>
          )} */}
          <TableRow data={data.titles} />
        </div>
        : <h1>данные не загружены</h1>
      }
    </div>
  )
};
export default App;