import { useEffect, useState } from 'react';
import './styles/App.css';
import InputComponent from './components/ui/InputComponent';
import ButtonComponent from './components/ui/ButtonComponent';


function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

const onload = e => {
  e.preventDefault();
  fetch('/api/get/',
    {
      headers: {
        'Content-Type': 'application/json;charset=utf-8',

      },
    }
  ).then(response => {
    if (response.ok) {
      return response.data
    } else {
      throw Error(`Something went wrong: code ${response.status}`)
    }
  })

}

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(true)
  const [loading, setLoading] = useState()
  const [form, setForm] = useState({ userName: '', password: '' })
  const [error, setError] = useState()
  const [data, setData] = useState({ firstName: '', lastName: '', userName: '', email: '', dateJoined: '' })
  const csrftoken = getCookie('csrftoken')


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
          setData({ firstName: data.first_name, lastName: data.last_name, userName: data.username, email: data.email, dateJoined: data.date_joined })
          setError(null)
        })
        .catch(error => {
          console.log(error)
          setError('Ошибка, подробности в консоли')
          setIsLoggedIn(false)
        })
    }
  }, [isLoggedIn])

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
          username: form.userName,
          password: form.password,
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
      .then(({ key }) => {
        setIsLoggedIn(true)
        setError(null)
      })
      .catch(error => {
        console.log(error)
        setError('Ошибка, подробности в консоли')
      })

      .finally(
        setLoading(false)

      )
  }

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
    setIsLoggedIn(false)
    setForm({ userName: '', password: '' })
  }


  return (
    <div className="App">

      <div className='login-block'>
        <form>
          <InputComponent 
            value={form.userName}
            onChange={e => setForm({ ...form, userName: e.target.value })}
            type='text' 
            placeholder='Username' 
          />
          <InputComponent 
            value={form.password}
            onChange={e => setForm({ ...form, password: e.target.value })}
            type='password' 
            placeholder='Password' 
          />
          <ButtonComponent onClick={submitHandler} >Login</ButtonComponent>
        </form>
      </div>

      <button onClick={onload}>getUser</button>
      {error ? <p>{error}</p> : null}
      {!isLoggedIn ?
        loading ? "Загрузка..." :
          <form className="loginForm" onSubmit={submitHandler}>
            <input type="text" name="username" value={form.userName} onChange={e => setForm({ ...form, userName: e.target.value })} placeholder="Username" />
            <input type="password" name="password" value={form.password} onChange={e => setForm({ ...form, password: e.target.value })} placeholder="Password" />
            <input type="submit" name="submit" value="Войти" />
          </form>
        :
        !error ?
          <div className="Profile">
            <div>
              <h1>{data.firstName} {data.lastName}</h1>
              <h2>{data.userName}</h2>
              <p>email: {data.email}</p>
              <p>Профиль создан {data.dateJoined}</p>
            </div>
            <div>
              <button className='button' onClick={logoutHandler}>LogOut</button>
            </div>
          </div>
          :
          null
      }
    </div>
  );
}
export default App;

