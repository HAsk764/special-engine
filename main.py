import requests


city = input('input your city ')
api_url = f'https://api.api-ninjas.com/v1/weather?city={city}'
response  = requests.get(api_url, headers={'X-Api-Key': '9fXieMqnK8+NGJPwPoC4WA==jOXvsfVQKaCpPEsR'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)