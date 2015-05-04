import unittest


from panda_network import PandaSocialNetwork, Panda, PandaAlreadyThere, PandasAlreadyFriends


class TestPandaSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.network = PandaSocialNetwork()
        self.test_panda = Panda("pandata", "pandata@gmail.com", "female")
        self.test_panda2 = Panda("pandata2", "pandata2@gmail.com", "male")
        self.network.add_panda(self.test_panda)
        self.network.make_friends(self.test_panda, self.test_panda2)

    def test_init(self):
        self.assertTrue(isinstance(self.test_panda, Panda))

    def test_add_panda(self):
        self.assertTrue(self.test_panda in self.network.list_of_pandas)

    def test_panda_already_added(self):
        with self.assertRaises(PandaAlreadyThere):
            self.network.add_panda(self.test_panda)

    def test_has_panda(self):
        self.assertTrue(self.test_panda in self.network.panda_friends)

    def test_make_friends(self):
        self.assertTrue(self.test_panda in self.network.panda_friends[self.test_panda2])

    def test_pandas_already_friends(self):
        with self.assertRaises(PandasAlreadyFriends):
            self.network.make_friends(self.test_panda, self.test_panda2)

    def test_are_friends(self):
        self.assertTrue(self.test_panda in self.network.panda_friends)

    def test_friends_of(self):
        self.assertTrue(self.test_panda in self.network.panda_friends[self.test_panda2])

    def test_connection_level(self):
        self.assertEqual(self.network.connection_level(self.test_panda, self.test_panda2), 1)

if __name__ == '__main__':
    unittest.main()
