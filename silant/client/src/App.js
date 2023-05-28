import { useState, useEffect } from 'react';
import './styles/App.css';

var arr = ['Яблоко', 'Банан'];


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
  const [user, setUser] = useState(' ')
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
      console.log(data.data[0])
      console.log(data.titles)
      setData(data)
      setError(null)
    }
    ).catch(error => {
      console.log(error)
      setError('Ошибка, подробности в консоли')
      setUser('')
    }
    )
  }, [user])

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
    e.preventDefault();
    fetch('api/logout/',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
          'X-CSRFToken': csrftoken,
        },
      }
    )
    setUser('')
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
      {error ? <p>{error}</p> : null}
      {!user ?
        loading ? "Загрузка..." :
          <form className="loginForm" onSubmit={submitHandler}>
            <input type="text" name="username" value={authForm.username} onChange={e => setAuthForm({ ...authForm, username: e.target.value })} placeholder="Username" />
            <input type="password" name="password" value={authForm.password} onChange={e => setAuthForm({ ...authForm, password: e.target.value })} placeholder="Password" />
            <input type="submit" name="submit" value="Войти" />
          </form>
        :
        !error ?
          <div className="Profile">
            <h1>1:{userData.firstName} {userData.lastName}</h1>
            <h2>2:{userData.username}</h2>
            <p>email: {userData.email}</p>
            <p>Профиль создан {userData.dateJoined}</p>
            <button className='button' onClick={logoutHandler}>logout</button>
          </div>
          :
          null
      }
      {
        user ? <h1>{user}</h1> : null
      }
      {data
        ?
        <div className='table-header'>
          <h3>заголовок</h3>
          <>
            {data.titles.map((item) => 
              <h3>{item}</h3>
            )}
          </>

        </div>
        : <h1>данные не загружены</h1>
      }
    </div>
  )
};
export default App;