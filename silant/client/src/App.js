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
  const [user, setUser] = useState()
  const [isLoggedIn, setIsLoggedIn] = useState(true)
  const [loading, setLoading] = useState()
  const [form, setForm] = useState({ userName: '', password: '' })
  const [error, setError] = useState()
  const [data, setData] = useState({ firstName: '', lastName: '', userName: '', email: '', dateJoined: '' })
  const csrftoken = getCookie('csrftoken')


  // useEffect(() => {
  //   if (isLoggedIn) {
  //     fetch(
  //       '/api/user/',
  //       {
  //         headers: {
  //           'Content-Type': 'application/json;charset=utf-8',

  //         },
  //       }
  //     )
  //       .then(response => {
  //         if (response.ok) {
  //           return response.json()
  //         } else {
  //           throw Error(`Something went wrong: code ${response.status}`)
  //         }
  //       })
  //       .then(({ data }) => {
  //         setData({ firstName: data.first_name, lastName: data.last_name, userName: data.username, email: data.email, dateJoined: data.date_joined })
  //         setError(null)
  //       })
  //       .catch(error => {
  //         console.log(error)
  //         setError('Ошибка, подробности в консоли')
  //         setIsLoggedIn(false)
  //       })
  //   }
  // }, [isLoggedIn])


  useEffect(() => {
    fetch(
      '/api/get/',
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
        setError(null)
      })
      .catch(error => {
        console.log(error)
        setError('Ошибка, подробности в консоли')
        setIsLoggedIn(false)
      })

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
    <div className="App" >
      {error ? <p>{error}</p> : null}
      {
        !isLoggedIn
          ?
          loading ? "Загрузка..."
            :
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
                <ButtonComponent onClick={submitHandler}>Login</ButtonComponent>
              </form>
            </div>
          :
          !error ?
            <div className="Profile">
              <div>
                <h2>{data.userName}</h2>
              </div>
              <div>
                <button className='button' onClick={logoutHandler}>LogOut</button>
              </div>
            </div>
            :
            null
      }
      <button onClick={onload}>getUser</button>
    </div>
  );
}
export default App;

