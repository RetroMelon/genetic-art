"""
generator.py - Joe Frew, 27/1/2015

The generator file contains constants and methods used to generate and mutate
genomes for images.

Some functionalities it provides are:

    generating single genomes at random from scratch.
    generating single genomes given parents and a weighting factor.
    mutating a genome given an amount to mutate by.
    generating an entire generation of genomes given some parent genomes.

This class contains constants which are:

    Number of circles per image.
    Circle Dimensions (ie. x, y, radius, red, green, blue, alpha)
    The length of a genetic code given the above factors.
    The length of a single circle in the genome given the able factors.
    The default generation size.
"""

import operator, random

#The number of circles per image.
NUMBER_OF_CIRCLES = 10

#The dimensionality of the image (xyr, colours(rgba)).
CIRCLE_DIMENSIONS = (3, 4)

#The number of bytes in the genetic code.
GENETIC_CODE_LENGTH = reduce(operator.mul, CIRCLE_DIMENSIONS) * NUMBER_OF_CIRCLES

#The number of bytes used to represent one circle.
CIRCLE_CODE_LENGTH = reduce(operator.add, CIRCLE_DIMENSIONS)

#The number of images in any one generation.
GENERATION_SIZE = 6

#The number of genomes per generation which should be completely new
NEW_GENOMES_PER_GENERATION = 2


def generate_generation(generation_size=GENERATION_SIZE, **kwargs):
    """
    Generates a list of genomes, the amount of which is dependent on the GENERATION-SIZE constant.
    The list of genomes can be a combination of the original parents, completely new genomes and
    mutations of the original parents.

    This function takes GENERATION_SIZE as an optional parameter and the following as kwargs:
        parent_genomes - a list of parent genomes.
        parent_weights - a list of weights that the parents hold on the child genomes.
        mutation_frequency - the amount of the genome to mutate. eg. 0.2 would be 1/5th of the genome.
        mutation_factor - the average factor that each gene mutates by.

    """

    print "generation_size", generation_size
    print "generate_genome kwargs", kwargs
    generate_genome(**kwargs)


def generate_genome(parent_genomes, parent_weights=[], **kwargs):
    """
    Generates a child genome based on a list of parent genomes. Can optionally mutate the genomes.

    This function takes these parameters:
        parent_genomes - a list of parent genomes.
        parent_weights - a list of weights that the parents hold on the child genomes.

    This function takes following as kwargs to pass to the mutate function:
        mutation_frequency - the amount of the genome to mutate. eg. 0.2 would be 1/5th of the genome.
        mutation_factor - the average factor that each gene mutates by.

    """

    #If the user did not provide any weights, make a default weights list.
    if len(parent_weights) == 0: #if the user did not provide any weights, set up defaults
        parent_weights = [1.0/len(parent_genomes)] * len(parent_genomes)
    elif sum(parent_weights) != 1.0:
        divisor = sum(parent_weights) * 1.0
        parent_weights = map(lambda x: x/divisor, parent_weights)


    return ["a"]*20


def mutate_genome(genome, mutation_frequency=0.2, mutation_factor=0.2):
    """
    Mutates some of the genes in a genome guided by the parameters.

    This function takes following parameters:
        genome - the genome the function is going to mutate.
        mutation_frequency - the amount of the genome to mutate. eg. 0.2 would be 1/5th of the genome.
        mutation_factor - the average factor that each gene mutates by.

    this method directly edits the list it is given, so it is advised to
    make a copy before calling if you don't want your genome to change.
    """

    for index, gene in enumerate(genome):
        if random.random() <= mutation_frequency:
            #mutating the gene
            new_gene = int(gene * (1 + random.choice([1, -1])*mutation_factor))

            #capping the gene at the limits
            if new_gene < 0:
                new_gene = 0
            elif new_gene > 255:
                new_gene = 255

            genome[index] = new_gene

    return genome

def generate_new_genome(genetic_code_length=GENETIC_CODE_LENGTH):
    """
    Generates a genome of the length specified.
    The max and min for each gene are 0 to 255.
    """
    return [random.randint(0, 255) for i in xrange(genetic_code_length)]
