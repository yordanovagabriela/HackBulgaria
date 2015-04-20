import unittest


from music_library import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Hit Em Up", "2Pac", "Greatest Hits", '2:54')

    def test_init(self):
        self.assertTrue(isinstance(self.song, Song))

    def test_validity_length(self):
        wrong_song = Song("2pac", "Greatest Hits", "Hit Em Up", '2')
        with self.assertRaises(ValueError):
            self.assertTrue(isinstance(wrong_song, Song))

    def test_get_seconds(self):
        self.assertEqual(self.song.get_seconds(), 174)

    def test_get_minutes(self):
        self.assertEqual(self.song.get_minutes(), 2)

    def test_get_hours(self):
        self.assertEqual(self.song.get_hours(), 0)

    def test_str(self):
        self.assertEqual(str(self.song),"Hit Em Up - 2Pac from Greatest Hits - 2:54")

    def test_hash(self):
        self.assertTrue(hash(self.song) == int(hash(self.song)))

    def test_eq(self):
        new_song = Song("Hit Em Up", "2Pac", "Greatest Hits", '2:54')
        self.assertEqual(self.song, new_song)

    def test_length_print(self):
        self.assertEqual(self.song.length_print(seconds=True), 174)
        self.assertEqual(self.song.length_print(minutes=True), 2)
        self.assertEqual(self.song.length_print(hours=True), 0)
        self.assertEqual(self.song.length_print(), '2:54')

if __name__ == '__main__':
    unittest.main()
