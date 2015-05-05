import os

from mutagen.mp3 import MP3


from mutagen.easyid3 import EasyID3


from music_library import Song, Playlist


import datetime


class MusicCrawler:

    def __init__(self, path):
        self.all_files_in_dir = os.listdir(path)
        self.mp3_files = [mp3 for mp3 in self.all_files_in_dir if mp3.endswith('mp3')]

    def generate_playlist(self):
        playlist = Playlist(name='Your-Songs', repeat=True, shuffle=False)
        for mp3_file in self.mp3_files:
            audio = MP3(mp3_file)
            artist = audio['TPE1']
            title = audio['TIT2']
            album = audio['TALB']
            length = str(datetime.timedelta(seconds=int(audio.info.length)))
            song = Song(artist=artist, title=title, album=album, length=length)
            playlist.add_song(song)
        return playlist.pprint_playlist()

crawler = MusicCrawler('/home/gabriela/Desktop/HackBulgaria/week4/MusicLibraryProject')
crawler.generate_playlist()
