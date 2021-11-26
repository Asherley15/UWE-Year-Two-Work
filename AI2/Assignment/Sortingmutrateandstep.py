
from matplotlib import pyplot as plt
import random
import numpy as np
import copy
import statistics
import math
from tabulate import *
N = 10
P = 50
fitnessscore = []
totalfitmut = 0
bestofrun = []
popscorelist = []
avgscorelist = np.array([])
listofaverage = []
np.set_printoptions(precision=5, suppress=True)


class individual:
    def __init__(self):
        self.gene = [0] * N
        self.fitness = 0


newind = individual()
population = []
yaxis = np.array([])
avgaxis = np.array([])

mutrate = 0.00
mutstep = 1.2


def test_func(ind):
    fitness = 0
    for x in range(N):
        fitness += (ind.gene[x]**2) - \
            (10 * (math.cos((2 * (math.pi)) * ind.gene[x])))
    return (10 * N) + fitness


numbertoavgover = 2
run = 0

xaxis = np.array([])
totalfitpop = 0
genz = 0
runs = 100
for a in range(3):
    mutstep += 0.2
    for z in range(10):
        if mutrate < 0.099:
            mutrate += 0.01
        else:
            mutrate = 0.01
        for x in range(numbertoavgover):
            run += 1
            population = []
            for gen in range(0, P):
                tempgene = []
                for y in range(0, N):
                    tempgene.append(random.uniform(-5.12, 5.12))
                newind = individual()
                newind.gene = tempgene.copy()
                population.append(newind)
                popbestscore = test_func(population[0])
            for currentrun in range(0, runs):
                popscorelist = []
                genz += 1
                counter = -1
                for x in population:
                    counter += 1
                    population[counter].fitness = test_func(x)
                offspring = []
                for i in range(0, P):
                    parent1 = random.randint(0, P - 1)
                    off1 = population[parent1]
                    parent2 = random.randint(0, P - 1)
                    off2 = population[parent2]
                    if off1.fitness > off2.fitness:
                        offspring.append(off2)

                    else:
                        offspring.append(off1)
                    counter = -1

                for x in offspring:
                    counter += 1
                    offspring[counter].fitness = test_func(x)
                totalfitpop = 0
                totalfitoff = 0

                counter = -1
                for x in population:
                    counter += 1
                    totalfitpop += population[counter].fitness
                counter = -1
                for x in offspring:
                    counter += 1
                    totalfitoff += offspring[counter].fitness

                crosspoint = random.randint(0, N - 1)
                z = 0

                for i in range(0, P, 2):

                    tempgene = offspring[i].gene.copy()

                    for k in range(0, crosspoint):
                        offspring[i].gene[k] = offspring[i + 1].gene[k]
                        offspring[i + 1].gene[k] = tempgene[k]

                mutatedgenes = []

                flip = 0.5
                for i in range(0, P):
                    newind = individual()
                    newind.gene = []
                    for j in range(0, N):
                        mutprob = random.random()
                        gene = offspring[i].gene[j]
                        if (mutprob) < (mutrate):
                            if random.random() < flip:
                                gene += mutstep
                                if gene > 5.12:
                                    gene = 5.12
                            else:
                                gene -= mutstep
                                if gene < -5.12:
                                    gene = -5.12
                        newind.gene.append(gene)
                    mutatedgenes.append(newind)

                totalfitmut = 0
                counter = -1

                for x in mutatedgenes:
                    counter += 1
                    totalfitmut += test_func(x)

                bestbaby = individual()
                bestbaby = population[0]
                for x in population:
                    if x.fitness < bestbaby.fitness:
                        bestbaby = x

                worsebaby = individual()
                worsebaby = population[0]
                for x in population:
                    if x.fitness > worsebaby.fitness:
                        worsebaby = x
                worsebaby = bestbaby
                fitnessscore.append(totalfitmut)
                population = copy.deepcopy(mutatedgenes)

                counter = -1
                for x in population:
                    counter += 1
                    population[counter].fitness = test_func(x)

                for x in population:
                    popscorelist.append(x.fitness)
                    if x.fitness <= popbestscore:
                        popbestscore = x.fitness

                yaxis = np.append(yaxis, popbestscore)

                avgpopscore = statistics.mean(popscorelist)
                avgscorelist = np.append(avgscorelist, avgpopscore)

                xaxis = np.append(xaxis, [genz])
                plt.plot(xaxis, yaxis, avgscorelist)
                # print(currentrun, popbestscore)
                print(popbestscore)
            print(currentrun, popbestscore)
            bestofrun.append(popbestscore)
            # for x in bestofrun:
            #     print(x)
            if len(bestofrun) == numbertoavgover:
                averageofruns = statistics.mean(bestofrun)
                bestofrun.clear()
                print("Still going...")
                listofaverage.append(
                    ["{:10.2f}".format(mutrate), "{:10.2f}".format(mutstep), averageofruns])
counter = 0

npversion = np.array(listofaverage)
table = tabulate(npversion, headers=[
                 "Index", "Mustep", "Mutrate", "Best Fitness"], showindex="always", tablefmt="pretty")
print(table)
currentbest = listofaverage[0]
for x in listofaverage:
    if x[2] < currentbest[2]:
        currentbest = x
print("BEST:\nMutstep:" +
      str(currentbest[0]) + "Mutrate:" + str(currentbest[1]) + "Score:" + str(currentbest[2]))
sorted = npversion[npversion[:, 2].argsort()]
tablesorted = tabulate(sorted, headers=[
    "Index", "Mustep", "Mutrate", "Best Fitness"], showindex="always", tablefmt="pretty")
print(tablesorted)
