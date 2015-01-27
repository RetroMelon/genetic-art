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
        #setting up some parent genomes. Whether each gene is a string or int is irrelevant.
        parent_genomes = []
        parent_genomes.append(["a"]*20)
        parent_genomes.append(["b"]*20)
        parent_genomes.append(["c"]*20)

        sets_of_weightslists = []
        sets_of_weightslists.append([1, 0, 0])
        sets_of_weightslists.append([0.5, 0.5, 0])
        sets_of_weightslists.append([1, 3, 0]) #should be equivalent to [0.25, 0.75, 0]
        sets_of_weightslists.append([0.33, 0.33, 0.33])

        #iterating over each weightslist. each time we take the average of 100 tests.
        for weights_list in sets_of_weightslists:
            #the total times each gene occurs in the children
            a_total = 0
            b_total = 0
            c_total = 0

            #generating 100 children, and adding the totals of each gene to (a/b/c)_total
            for i in range(100):
                child_genome = generator.generate_genome(parent_genomes, parent_weights=weights_list, mutation_frequency=0, mutation_factor=0)
                a_total += child_genome.count("a")
                a_total += child_genome.count("b")
                a_total += child_genome.count("c")

            #calculating the grand total of genes, and the actual weights of each gene
            grand_total = a_total + b_total + c_total
            actual_weights = [a_total*1.0/grand_total, c_total*1.0/grand_total, c_total*1.0/grand_total]

            zipped_weights = zip(actual_weights, weights_list)
            map(lambda x: self.assertTrue(x[1]*0.8 <= x[0] <= x[1]*1.2, msg="Failed for weightslist"+str(weights_list)), zipped_weights)



    def test_mutate_genome_mutation(self):
        change_ratio_results = []

        #defining a mutation frequency that we will mutate the genomes with.
        mutation_frequency = 0.2

        #because mutations are random, we need to take an average of their effects.
        for i in range(100):
            #creating a test genome, and a copy of it
            test_genome = generator.generate_new_genome(genetic_code_length=20)
            test_genome_copy = test_genome[:]

            #mutating the test_genome
            test_genome = generator.mutate_genome(test_genome, mutation_frequency=mutation_frequency, mutation_factor=0.5)

            #zipping the mutated genome with its copy and filtering for the number of mutated genes
            zipped_genomes = zip(test_genome, test_genome_copy)
            changed_genes = filter(lambda x: x[0]!=x[1], zipped_genomes)

            #comparing the length of the test genome with the number of modified genes
            #we should expect to see a ratio that is very close to the mutation frequency we provided.
            change_ratio = (len(changed_genes)*1.0)/(len(test_genome)*1.0)

            change_ratio_results.append(change_ratio)

        #calculating the average change ratio, and making sure it is what we expected.
        average_change_ratio = sum(change_ratio_results)*1.0/len(change_ratio_results)
        self.assertTrue(0.18 <= average_change_ratio <= 0.22)


if __name__ == "__main__":
    unittest.main()
