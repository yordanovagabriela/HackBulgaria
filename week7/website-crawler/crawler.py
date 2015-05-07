from bs4 import BeautifulSoup


import requests


import json


class Crawler:

    def __init__(self):
        self.our_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        }
        self.url = 'http://register.start.bg/'
        self.links = []
        self.actual_locations = []
        self.servers = []

    def crawl_all_links(self):
        r = requests.get(self.url, headers=self.our_headers)
        soup = BeautifulSoup(r.text)
        for link in soup.find_all('a'):
            self.links.append(link.get('href'))

    def classify(self):
        classified_links = []
        for link in self.links:
            if link is not None:
                if '.php?id' in link:
                    classified_links.append(link)
        return classified_links

    def find_actual_location(self):
        urls = self.classify()
        for php in urls:
            req = requests.head('{}{}'.format(self.url, php), headers=self.our_headers, timeout=4)
            self.actual_locations.append(req.headers["Location"])

    def get_servers(self):
        for url in self.actual_locations:
            try:
                req = requests.head(url, headers=self.our_headers)
                self.servers.append(req.headers["Server"])
            except Exception:
                pass

    def save_servers(self):
        servers = json.dumps(self.servers)
        with open('servers.json', 'r') as file:
            file.write(servers)


def main():
    crawler = Crawler()
    crawler.crawl_all_links()
    crawler.classify()
    crawler.find_actual_location()
    crawler.get_servers()
    crawler.save_servers()

if __name__ == '__main__':
    main()
