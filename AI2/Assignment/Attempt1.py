
from matplotlib import pyplot as plt
import random
import matplotlib
import numpy as np
import copy
import statistics
import math
from tabulate import tabulate

recordarray = []
# Initialise population (P) and geneome length(N)
N = 10
P = 50
runavg = []
# Declare NP array to hold the average fitness of generations, best score and X axis (no of gens ran)
avgscorelist = np.array([])
bestscorelist = []
xaxis = np.array([])
# Define the inidividual gene class.
mutstepofgen = []
testarray = []
f = open("/Users/ashleypearson/Documents/UWE/Year Two/AI2/Assignment/runresults.txt", "w")
f.write("Mutrate   MutSTEP   Score\n")


class individual:
    def __init__(self):
        self.gene = [0] * N
        self.fitness = 0


def test_func(ind):
    fitness = 0
    # Loop through each genome in the individual(N)
    for x in range(N):
        fitness += (ind.gene[x]**2) - \
            (10 * (math.cos((2 * (math.pi)) * ind.gene[x])))
    return (10 * N) + fitness


for z in range(10):
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
        mutstep = 0.05
        lastofgenaverage = []
        for k in range(19):
            mutstep += 0.05
            lastofgenaverage = []
            avgofgenscores = []
            # loop through population size and create p number total individuals.
            for gen in range(0, P):
                tempgene = []
                # within each individual assign a random gene value given below (-5.12-5.12)
                for y in range(0, N):
                    tempgene.append(random.uniform(-5.12, 5.12))
                newind = individual()
                newind.gene = tempgene.copy()
                # Append individual to the population.
                population.append(newind)

            # Fitness Function(pass an individual)

            ################PRIMARY LOOP BEGINS####################
            for gencheck in range(0, 100):
                popbestscore = test_func(population[0])
                # Pick best fitness in initial population to create graph.
                print("BEGINNING POPBESTSCORE:", popbestscore)

                for x in population:
                    if test_func(x) <= popbestscore:
                        popbestscore = test_func(x)
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
                            # 50% chance to add or subtract mutstep amount.
                            if random.random() < 0.5:
                                gene += mutstep
                                if gene > 5.12:
                                    gene = 5.12
                            else:
                                gene -= mutstep
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

                avgscorelist = np.append(
                    avgscorelist, statistics.mean(popscorelist))

                xaxis = np.append(xaxis, [gencheck])
                if gencheck == P:
                    genbest.append(popbestscore)

                mutstepofgen.append(mutstep)
                mutrateofgen.append(mutrate)
                lastofgenaverage.append(popbestscore)
                print(len(lastofgenaverage))
                bestscorelist.append(popbestscore)
                print(avgofgenscores)
                if len(lastofgenaverage) == 2:
                    avgofgenscores = statistics.mean(lastofgenaverage)
                print(mutrate, mutstep, avgofgenscores)
            testarray.append([mutrate, mutstep, avgofgenscores])

    for x in testarray:
        print("MUTERATE", x[0], "MUTSTEP:", x[1], "avg best score:", x[2])
    print(len(testarray))

    currentbest = testarray[0]
    for x in testarray:
        if x[2] < currentbest[2]:
            currentbest = x
    testarray.clear()
    print("muterate:", currentbest[0], "mutestep",
          currentbest[1], "best score", currentbest[2])
    test = ((currentbest[0]),
            (currentbest[1]), (currentbest[2]))
    print(test)
    recordarray.append(test)
    f.write(str(test) + '\n')
f.write("\n")

lowest = recordarray[0]
for x in recordarray:
    print(x)
    if x[2] < lowest[2]:
        lowest = x
print("best:", lowest)
f.close()
