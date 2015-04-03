import unittest


from panda_network import Panda


class TestPandaNetwork(unittest.TestCase):

    def setUp(self):
        self.test_panda = Panda("pandata", "pandata@gmail.com", "female")

    def test_init(self):
        self.assertTrue(isinstance(self.test_panda, Panda))

    def test_str(self):
        self.assertEqual(str(self.test_panda), "pandata")

    def test_repr(self):
        self.assertEqual(str(self.test_panda), "pandata")

    def test_eq(self):
        new_panda = Panda("pandata", "pandata@gmail.com", "female")
        self.assertTrue(new_panda == self.test_panda)

    def test_hash(self):
        self.assertTrue(hash(self.test_panda) == int(hash(self.test_panda)))

    def test_male(self):
        male_panda = Panda("f", "ddd@abv.bg", "male")
        self.assertEqual(male_panda.gender, "male")

    def test_female(self):
        self.assertEqual(self.test_panda.gender, "female")

if __name__ == '__main__':
    unittest.main()
