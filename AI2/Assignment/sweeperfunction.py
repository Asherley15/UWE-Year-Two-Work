
from matplotlib import pyplot as plt
import random
import numpy as np
import copy
import statistics
import math
from tabulate import *
import json
import time
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
mutstep = 0.00
startingmutrate = mutrate
startingmutstep = mutstep
numbertoavgover = int(input("Number of generation runs to average over: "))
mutstepincreases = int(input("Enter No of Mutstep increments:"))
mutstepincrement = float(input("Enter the value of each Mutstep increment: "))
mutrateincreases = int(input("Enter No of Mutrate increments:"))
mutrateincrement = float(input("Enter the value of each Mutrate increment: "))
runs = int(input("Enter the number of generations to run for: "))

GAsettings = {"Starting mutrate: ": startingmutrate, "Starting mutstep": startingmutstep, "Number of runs to average over": numbertoavgover,
              "No of mutstep increases": mutstepincreases, "No of mutrate increases": mutrateincreases, "Size of mutrate increases": mutrateincrement, "Size of mutstep": mutstepincrement, "Number of generations": runs}


def test_func(ind):
    fitness = 0
    for x in range(N):
        fitness += (ind.gene[x]**2) - \
            (10 * (math.cos((2 * (math.pi)) * ind.gene[x])))
    return (10 * N) + fitness


run = 0
count = 0
totalfitpop = 0
start = time.time()
for a in range(mutstepincreases):
    mutstep += mutstepincrement
    for z in range(mutrateincreases):
        if mutrate < 0.099:
            mutrate += mutrateincrement
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

                # for x in offspring:
                #     counter += 1
                #     offspring[counter].fitness = test_func(x)
                # totalfitpop = 0
                # totalfitoff = 0

                # counter = -1
                # for x in population:
                #     counter += 1
                #     totalfitpop += population[counter].fitness
                # counter = -1
                # for x in offspring:
                #     counter += 1
                #     totalfitoff += offspring[counter].fitness

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

                print("BEST: ", popbestscore)
                for x in population:
                    popscorelist.append(x.fitness)
                    if x.fitness <= popbestscore:
                        popbestscore = x.fitness

                yaxis = np.append(yaxis, popbestscore)

                avgpopscore = statistics.mean(popscorelist)
                avgscorelist = np.append(avgscorelist, avgpopscore)

                # print(currentrun, popbestscore)
                count += 1
                print(count)
            bestofrun.append(popbestscore)
            for x in bestofrun:
                print(x)
            if len(bestofrun) == numbertoavgover:
                averageofruns = statistics.mean(bestofrun)
                print("avg:", averageofruns)
                bestofrun.clear()
                print("Still going...")
                listofaverage.append(
                    ["{:10.2f}".format(mutrate), "{:10.2f}".format(mutstep), averageofruns])
end = time.time()

f = open("/Users/ashleypearson/Documents/UWE/Year Two/AI2/Assignment/runresults.txt", "w")
f.write("-----------------GA Results-----------------\nSettings as follows:\n")
f.write(json.dumps(GAsettings) + "\n")
npversion = np.array(listofaverage)
table = tabulate(npversion, headers=[
                 "Index", "Murate", "Mutstep", "Best Fitness"], showindex="always", tablefmt="pretty")
print(table)
currentbest = listofaverage[0]
for x in listofaverage:
    if x[2] < currentbest[2]:
        currentbest = x
print("BEST:\nMutstep:" +
      str(currentbest[0]) + "Mutrate:" + str(currentbest[1]) + "Score:" + str(currentbest[2]))
sorted = npversion[npversion[:, 2].argsort()]
tablesorted = tabulate(sorted, headers=[
    "Index", "Mutrate", "Mutstep", "Best Fitness"], showindex="always", tablefmt="pretty")
print(tablesorted)
elapsed = end - start
print("BEST:\nMutstep:" +
      str(currentbest[0]) + "Mutrate:" + str(currentbest[1]) + "Score:" + str(currentbest[2]))
f.write("Unsorted data:\n" + table + "\n")
f.write("Sorted table: \n" + tablesorted + "\n")
f.write(str(currentbest) + "\nTime to run: " + str(elapsed / 60) + " minutes")
f.close()
