import requests

r = requests.get('https://api.github.com/users/yordanovagabriela?client_id=378faee748383b4d5290&client_secret=0f5e45f7526789f077e9b0d2e052718b5122aecc').json()
print(r['following_url'])
