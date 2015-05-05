import unittest


from music_library import Song, Playlist


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.p = Playlist(name='my_playlist')
        self.song = Song(artist='bebe', title='bebeto', album='tobebeto', length='3:21')

    def test_init(self):
        self.assertTrue(isinstance(self.p), Playlist)

    def test_add_song(self):
        pass

    def test_remove_song(self):
        pass

    def test_add_songs(self):
        pass

    def test_artists(self):
        pass

    def test_next_song(self):
        pass

    def test_total_length(self):
        pass

if __name__ == '__main__':
    unittest.main()
