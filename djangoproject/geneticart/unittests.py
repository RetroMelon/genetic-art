"""
A series of unit tests for the non-django parts of the application.
eg. generator.py
"""
import unittest

#importing the modules that we will be testing
import generator

class TestGenerator(unittest.TestCase):

    def setUp(self):
        pass #self.test_genomes = [generator.gerate_new_genome() for i in range(3)]

    def generate_generation_(self):
        generator.generate_generation(parent_genomes=["hi", "hey", "hello"], parent_weights=[1, 2, 3], mutation_chance=0.5, mutation_factor=0.2)

        # should raise an exception for an immutable sequence
        #self.assertRaises(TypeError, random.shuffle, (1,2,3))
        return True

    def test_generate_genome(self):
        return
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_mutate_genome_mutation(self):
        change_ratio_results = []

        #because mutations are random, we need to take an average of their effects.
        for i in range(100):
            #creating a test genome, and a copy of it
            test_genome = generator.generate_new_genome(genetic_code_length=20)
            test_genome_copy = test_genome[:]

            #defining a mutation frequency that we will mutate the genomes with.
            mutation_frequency = 0.2

            #mutating the test_genome
            test_genome = generator.mutate_genome(test_genome, mutation_frequency=mutation_frequency, mutation_factor=0.5)

            #zipping the mutated genome with its copy and filtering for the number of mutated genes
            zipped_genomes = zip(test_genome, test_genome_copy)
            changed_genes = filter(lambda x: x[0]!=x[1], zipped_genomes)

            #comparing the length of the test genome with the number of modified genes
            #we should expect to see a ratio that is very close to the mutation frequency we provided.
            change_ratio = (len(changed_genes)*1.0)/(len(test_genome)*1.0)

            change_ratio_results.append(change_ratio)

        average_change_ratio = sum(change_ratio_results)*1.0/len(change_ratio_results)
        self.assertTrue(0.18 <= average_change_ratio <= 0.22)


if __name__ == "__main__":
    unittest.main()
