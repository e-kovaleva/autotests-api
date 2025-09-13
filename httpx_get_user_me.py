import httpx


login_payload = {
  'email': 'user@email.com',
  'password': 'password'
}
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
access_token = login_response_data['token']['accessToken']

print('Login status code:', login_response.status_code)


headers = {'Authorization': f'Bearer {access_token}'}
me_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=headers)

print('Me status code:', me_response.status_code)
print(me_response.json())
