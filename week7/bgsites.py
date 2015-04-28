import httplib2


from bs4 import BeautifulSoup, SoupStrainer


import requests


import json


class Histogram:
    def __init__(self):
        self.items = {}

    def add(self, word):
        if word not in self.items:
            self.items[word] = 1
        else:
            self.items[word] += 1

    def count(self, word):
        return self.items[word]

    def get_dict(self):
        return self.items

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
    req = requests.head('http://register.start.bg/{}'.format(url), headers=our_headers, timeout=200)
    actual_location.append(req.headers["Location"])


# # save .php links to json
# json_str = json.dumps(urls)
# with open('websites.json', "w") as f:
#     f.write(json_str)

# save actual_location to json
json_loc = json.dumps(actual_location)
with open('ActualLocation.json', "w") as f:
    f.write(json_loc)
