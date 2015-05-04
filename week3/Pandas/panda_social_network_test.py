import unittest


from panda_network import PandaSocialNetwork, Panda


class TestPandaSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.test_panda = Panda("pandata", "pandata@gmail.com", "female")

    def test_init(self):
        self.assertTrue(isinstance(self.test_panda, Panda))

if __name__ == '__main__':
    unittest.main()
