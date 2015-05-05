from prettytable import PrettyTable


import datetime


import json


import random


import time


class NoMoreSongs(Exception):
    pass


class SongAlreadyInPlaylist(Exception):
    pass


class Song:

    def __init__(self, artist, title, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        times = [int(x) for x in length.split(":")]
        if len(times) == 3:
            self.length = length
            self.hours = times[0]
            self.minutes = times[1]
            self.seconds = times[2]
        elif len(times) == 2:
            self.length = length
            self.minutes = times[0]
            self.seconds = times[1]
        else:
            raise ValueError

    def get_seconds(self):
        return self.seconds + self.minutes*60 + self.hours*3600

    def get_minutes(self):
        return self.minutes + self.hours*60

    def get_hours(self):
        return self.hours

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __eq__(self, other):
        is_artist = self.artist == other.artist
        is_title = self.title == other.title
        is_album = self.album == other.album
        is_length = self.length == other.length
        return is_artist and is_title and is_album and is_length

    def __hash__(self):
        return hash(self.__str__())

    def length_print(self, seconds=False, minutes=False, hours=False):
        if not seconds and not minutes and not hours:
            return self.length
        if hours:
            return self.get_hours()
        if minutes:
            return self.get_minutes()
        if seconds:
            return self.get_seconds()

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict if not key.startswith("_")}


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.playlist = []
        self.artist_dict = {}
        self.counter = -1
        self.shuffle_songs = set()

    def add_song(self, song):
# MusicCrawler gets error ?
        # if song in self.playlist:
        #     raise SongAlreadyInPlaylist("The song is already in the playlist")
        # else:
        self.playlist.append(song)
            # if song.artist in self.artist_dict:
            #     self.artist_dict[song.artist] += 1
            # else:
            #     self.artist_dict[song.artist] = 1

    def remove_song(self, song):
        self.playlist.remove(song)
        if self.artist_dict[song.artist] != 1:
            self.artist_dict[song.artist] -= 1
        else:
            del self.artist_dict[song.artist]

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def artists(self):
        return self.artist_dict

    def shuffleit(self):
        rsong = random.choice(self.playlist)
        while rsong in self.shuffle_songs:
            rsong = random.choice(self.playlist)
        self.shuffle_songs.add(rsong)
        if len(self.shuffle_songs) == len(self.playlist):
            self.shuffle_songs = set()
        return rsong

    def next_song(self):
        self.counter += 1
        if self.repeat is True:
            if self.shuffle is True:
                return self.shuffleit()
            else:
                try:
                    return self.playlist[self.counter]
                except:
                    self.counter = 0
                    return self.playlist[self.counter]
        else:
            try:
                return self.playlist[self.counter]
            except:
                raise NoMoreSongs("There are no more songs in the playlist!")

    def total_length(self):
        sum_seconds = sum([song.length_print(seconds=True) for song in self.playlist])
        return str(datetime.timedelta(seconds=sum_seconds))

    def pprint_playlist(self):
        t = PrettyTable(['Artist', 'Song', 'Length'])
        for song in self.playlist:
            t.add_row([song.artist, song.title, song.length])
        print(t)

    def prepare_json(self):
        data = {
            "name": self.name,
            "songs": [song.prepare_json() for song in self.playlist]
        }

        return data

    def save(self, indent=True):
        filename = self.name.replace(" ", "-") + ".json"
        with open(filename, "w+") as f:
            f.write(json.dumps(self.prepare_json(), indent=indent))

    @staticmethod
    def load(filename):
        with open('./playlist-data/' + filename, "r") as f:
            contents = f.read()
            data = json.loads(contents)
            p = Playlist(data["name"])

            for dict_song in data["songs"]:
                song = Song(artist=dict_song["artist"], title=dict_song["title"], album=dict_song["album"], length=dict_song["length"])
                p.add_song(song)

            return p


def test_load():
    p = Playlist.load("Manowar-songs.json")
    try:
        while True:
            song = p.next_song()
            print(str(song))
            time.sleep(1)
    except Exception as e:
        print(e)


s = Song(album="The Sons of Odin", title="Odin", artist="Manowar", length="3:44")
s1 = Song(album="The Sonds of Odin", title="Sons of Odin", artist="Manowar", length="6:08")
p = Playlist("Manowar songs", repeat="SONG")
p.add_song(s)
p.add_song(s1)
p.add_song(Song(album="Fallen", title="Bring Me To Life (radio edit)", artist="Evanesence", length="3:30"))
p.pprint_playlist()
p.save()
