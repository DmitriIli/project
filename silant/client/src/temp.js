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



  useEffect(() => {
    fetch(
      '/api/get/',
      {
        headers: {
          'Content-Type': 'application/text;charset=utf-8',
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
      .then(({context_data}) => {
        setError(null)
      })
      .catch(error => {
        console.log(error)
        setError('Ошибка, подробности в консоли')
        setIsLoggedIn(false)
      })

  }, [isLoggedIn])