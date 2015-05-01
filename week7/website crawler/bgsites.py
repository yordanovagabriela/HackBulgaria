from bs4 import BeautifulSoup


import requests


import json


our_headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
}

# find all .php links from start.bg

r = requests.get('http://register.start.bg', headers=our_headers)
soup = BeautifulSoup(r.text)
urls = [link.get('href') for link in soup.find_all('a') if((link.get('href')) != None and '.php?id' in link.get('href'))]

#find the actual location of the links
actual_location = []
for url in urls:
    req = requests.head('http://register.start.bg/{}'.format(url), headers=our_headers, timeout=4)
    actual_location.append(req.headers["Location"])


# # save .php links to json
# json_str = json.dumps(urls)
# with open('websites.json', "w") as f:
#     f.write(json_str)

# save actual_location to json
json_loc = json.dumps(actual_location)
with open('ActualLocation.json', "w") as f:
    f.write(json_loc)
