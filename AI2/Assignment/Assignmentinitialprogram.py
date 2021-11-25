
from matplotlib import pyplot as plt
import random
import matplotlib
import numpy as np
import copy
import statistics
import math
from tabulate import tabulate
# Initialise population (P) and geneome length(N)
N = 10
P = 50
runavg = []
# Declare NP array to hold the average fitness of generations, best score and X axis (no of gens ran)
avgscorelist = np.array([])
bestscorelist = np.array([])
xaxis = np.array([])
timer = 0
# Define the inidividual gene class.


class individual:
    def __init__(self):
        self.gene = [0] * N
        self.fitness = 0


# Create an individual.
newind = individual()
# Set Mutation rate
mutrate = 0.00
genbest = []
mutrateofgen = []

# Create population array
population = []
for j in range(10):
    mutrate += 0.01
    lastofgenaverage = []
    for k in range(10):
        # loop through population size and create p number total individuals.
        for gen in range(0, P):
            timer += 1
            tempgene = []
            # within each individual assign a random gene value given below (-5.12-5.12)
            for y in range(0, N):
                tempgene.append(random.uniform(-5.12, 5.12))
            newind = individual()
            newind.gene = tempgene.copy()
            # Append individual to the population.
            population.append(newind)

        # Fitness Function(pass an individual)

        def test_func(ind):
            fitness = 0
            # Loop through each genome in the individual(N)
            for x in range(N):
                fitness += (ind.gene[x]**2) - \
                    (10 * (math.cos((2 * (math.pi)) * ind.gene[x])))
            return (10 * N) + fitness

        popbestscore = 2000
        # Pick best fitness in initial population to create graph.
        for x in population:
            if test_func(x) <= popbestscore:
                popbestscore = test_func(x)

        ################PRIMARY LOOP BEGINS####################
        for gencheck in range(0, 100):
            popscorelist = []
            counter = -1
            for x in population:
                counter += 1
                population[counter].fitness = test_func(x)

        # Offspring array
            offspring = []
            # Selection function, pick 2 random parents, pick the better gene and add it to the offspring array
            for i in range(0, P):
                parent1 = random.randint(0, P - 1)
                off1 = population[parent1]
                parent2 = random.randint(0, P - 1)
                off2 = population[parent2]
                if off1.fitness > off2.fitness:
                    offspring.append(off2)
                else:
                    offspring.append(off1)

        # Pick a random point around which to swap genome values(CROSSOVER)
            crosspoint = random.randint(0, N - 1)
            for i in range(0, P, 2):
                tempgene = offspring[i].gene.copy()
                for k in range(0, crosspoint):
                    offspring[i].gene[k] = offspring[i + 1].gene[k]
                    offspring[i + 1].gene[k] = tempgene[k]

        # initialise array for mutated genes
            mutatedgenes = []

        # Set value to tweak gene by if triggered.
            alter = random.random()
        # Loop through population
            for i in range(0, P):
                newind = individual()
                newind.gene = []
                # loop through individidual genes
                for j in range(0, N):
                    mutprob = random.random()
                    gene = offspring[i].gene[j]
                    # Chance to mutate each individual gene:
                    if random.random() < (mutrate):
                        # 50% chance to add or subtract alter amount.
                        if random.random() < 0.5:
                            gene += alter
                            if gene > 5.12:
                                gene = 5.12
                        else:
                            gene -= alter
                            if gene < -5.12:
                                gene = -5.12

                    # Add altered genes to mutatedgenes array.
                    newind.gene.append(gene)
                mutatedgenes.append(newind)

            # initialise worst and best baby individuals.
            worsebaby = population[0]
            bestbaby = population[0]
            # Loops through the mutated genes array
            for x in mutatedgenes:
                # If current fitness is better than existing best,replace.
                if test_func(x) < test_func(bestbaby):
                    bestbaby = x
                # If current fitness is better than existing worst,replace.
                if test_func(x) > test_func(worsebaby):
                    worsebaby = x
                    indexno = mutatedgenes.index(worsebaby)

            mutatedgenes[indexno] = bestbaby
            population = copy.deepcopy(mutatedgenes)

            counter = -1
            for x in population:
                counter += 1
                population[counter].fitness = test_func(x)

            for x in population:
                popscorelist.append(x.fitness)
                if x.fitness <= popbestscore:
                    popbestscore = x.fitness

            bestscorelist = np.append(bestscorelist, popbestscore)

            avgscorelist = np.append(
                avgscorelist, statistics.mean(popscorelist))

            xaxis = np.append(xaxis, [gencheck])
            if gencheck == P:
                genbest.append(popbestscore)
        lastofgenaverage.append(popbestscore)
    mutrateofgen.append(mutrate)

    counter = 0

    avgofgenscores = statistics.mean(lastofgenaverage)
    runavg.append(avgofgenscores)
    print()

mydata = [mutrateofgen, runavg]
print(tabulate(mydata))
