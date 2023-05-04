import { useEffect, useState } from 'react';
import './App.css';


function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(true)
  const [loading, setLoading] = useState()
  const [formUsername, setFormUsername] = useState()
  const [formPassword, setFormPassword] = useState()
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [dateJoined, setDateJoined] = useState('')
  const [error, setError] = useState()
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
          setFirstName(data.first_name)
          setLastName(data.last_name)
          setUsername(data.username)
          setEmail(data.email)
          setDateJoined(data.date_joined)
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
          username: formUsername,
          password: formPassword
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
    setFormUsername('')
    setFormPassword('')
    
  }
  return (
    <div className="App">
      {error ? <p>{error}</p> : null}
      {!isLoggedIn ?
        loading ? "Загрузка..." :
          <form className="loginForm" onSubmit={submitHandler}>
            <input type="text" name="username" value={formUsername} onChange={e => setFormUsername(e.target.value)} placeholder="Username" />
            <input type="password" name="password" value={formPassword} onChange={e => setFormPassword(e.target.value)} placeholder="Password" />
            <input type="submit" name="submit" value="Войти" />
          </form>
        :
        !error ?
          <div className="Profile">
            <div>
              <h1>{firstName} {lastName}</h1>
              <h2>{username}</h2>
              <p>email: {email}</p>
              <p>Профиль создан {dateJoined}</p>
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

