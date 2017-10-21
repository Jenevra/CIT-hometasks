import json
import requests

data = {'registration data': 'Pankratova Evgeniia'}
header = {'Content-Type': 'application/json'}

host = 'https://cit-home1.herokuapp.com'
register = '/api/register'
check = '/api/check_me'

request = requests.post(host + register, json.dumps(data), headers=header)

check_request = requests.get(host + check)
print(check_request.json())
