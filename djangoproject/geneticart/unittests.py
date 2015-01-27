"""
A series of unit tests for the non-django parts of the application.
eg. generator.py
"""
import unittest

#importing the modules that we will be testing
import generator

class TestGenerator(unittest.TestCase):

    def setUp(self):
        pass

    def generate_generation_(self):
        generator.generate_generation(parent_genomes=["hi", "hey", "hello"], parent_weights=[1, 2, 3], mutation_chance=0.5, mutation_factor=0.2)

        # should raise an exception for an immutable sequence
        #self.assertRaises(TypeError, random.shuffle, (1,2,3))
        return True

    def test_generate_genome(self):
        return
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_mutate_genome(self):
        return
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


if __name__ == "__main__":
    unittest.main()
