import requests

from Graph import DirectedGraph

import json


class User:

    def __init__(self, username):
        CLIENT_ID = '378faee748383b4d5290'
        CLIENT_SECRET = '0f5e45f7526789f077e9b0d2e052718b5122aecc'

        self.usernam = username
        self.user_info = requests.get("https://api.github.com/users/{}".format(username)).json()
        self.login = self.user_info['login']
        self.followers_url = '''https://api.github.com/users/{}/followers?client_id={}&client_secret={}'''.format(username, CLIENT_ID, CLIENT_SECRET)
        self.following_url = '''https://api.github.com/users/{}/following?client_id={}&client_secret={}'''.format(username, CLIENT_ID, CLIENT_SECRET)
        self.followers = requests.get(self.followers_url).json()
        self.following = requests.get(self.following_url).json()
        self.graph = DirectedGraph(username)
