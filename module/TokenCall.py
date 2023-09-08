import requests


formdata = {
  'grant_type': 'authorization_code',
  'code': '<code>',
  'redirect_uri': 'https://notify-bot.line.me/my/services/new',
  'client_id': 'BAqdeKIM65ngYYhDVRr57o',
  'client_secret': 'syT4cJVbq3htZKcfoxTZ4cR1jAJhooM63rGvEtv8jyQ'
}

params = '&'.join([f"{key}={value}" for key, value in formdata.items()])

url = 'https://notify-bot.line.me/oauth/token'

headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(url, headers=headers, data=params)

if response.status_code == 200:
  data = response.json()
  print(data['access_token'])
else:
  print('Error:', response.status_code)
  print(response.text)
