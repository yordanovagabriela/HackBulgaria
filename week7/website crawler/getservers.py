import requests


import json


our_headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
}

servers = []
with open('ActualLocation.json', 'r') as f:
    data = json.load(f)
for url in data:
    try:
        req = requests.head(url, headers=our_headers)
        servers.append(req.headers["Server"])
    except Exception:
        pass
json_str = json.dumps(servers)
with open('servers.json', "w") as f:
    f.write(json_str)
