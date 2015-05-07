from histogram import Histogram


import json


import matplotlib.pyplot as plt


histogram = Histogram()

with open('servers.json', 'r') as f:
    data = json.load(f)
data = [server.encode('utf-8') for server in data]
for server in data:
    if 'Apache' in server or 'Apashi' in server:
        histogram.add('Apache')
    elif 'nginx' in server:
        histogram.add('nginx')
    elif 'lighttpd' in server:
        histogram.add('lighttpd')
    elif 'IIS' in server:
        histogram.add('IIS')


plt.bar(range(len(histogram.get_dict())), histogram.get_dict().values(), align='center')
plt.xticks(range(len(histogram.get_dict())), histogram.get_dict().keys())
print(plt.show())
