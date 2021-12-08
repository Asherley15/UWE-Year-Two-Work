
from typing import final
from matplotlib import pyplot as plt
import random
import numpy as np
import copy
import statistics
import math
from numpy.core.fromnumeric import size, sort
from tabulate import *
import json
import time
from mpl_toolkits.mplot3d import Axes3D


class individual:
    def __init__(self):
        self.gene = [0] * N
        self.fitness = 0


global N, P
N = 20
P = 50

np.set_printoptions(precision=5, suppress=True)


def selection():


def pop_init():
    for gen in range(0, P):
        tempgene = []
        for y in range(0, N):
            tempgene.append(random.uniform(-10, 10))
        newind = individual()
        newind.gene = tempgene.copy()
        population.append(newind)
    return population


def test_func(ind, N):
    fitness = 0
    fitnesstotal = 0
    fitnessarray = []
    first = (ind.gene[0] - 1)**2
    for i in range(1, N):
        fitness += i * (((2 * ind.gene[i]**2) - (ind.gene[i - 1]))**2)
        fitness = fitness + first
        fitnessarray.append(fitness)
        fitnesstotal += fitness
    return fitnessarray, fitnesstotal, fitness


def scoreplotter(N, P, test_func, mutrate, mutstep):
    popscorelist = []
    avgscorelist = []

    newind = individual()
    population = []
    yaxis = []

    population = pop_init()

    xaxis = []

    genz = 0
    runs = 100
    popbestscore = test_func(population[0], N)

    for currentrun in range(0, runs):
        popscorelist = []
        genz += 1
        counter = -1

        for x in population:
            counter += 1
            fitscore = test_func(x, N)
            population[counter].fitness = fitscore[2]

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

        crosspoint = random.randint(0, N - 1)

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
                        if gene > 10:
                            gene = 10
                    else:
                        gene -= mutstep
                        if gene < -10:
                            gene = -10
                newind.gene.append(gene)
            mutatedgenes.append(newind)

        counter = -1

        for x in mutatedgenes:
            fitscore = test_func(x, N)
            x.fitness = fitscore[2]

        worsebaby = mutatedgenes[0]
        bestbaby = mutatedgenes[0]

        for x in mutatedgenes:
            if x.fitness < bestbaby.fitness:
                bestbaby = x

        for x in mutatedgenes:
            if x.fitness > worsebaby.fitness:
                worsebaby = x
        indexno = mutatedgenes.index(worsebaby)
        mutatedgenes[0] = bestbaby
        population = copy.deepcopy(mutatedgenes)

        counter = -1

        popbestscore = population[0].fitness

        for x in population:
            counter += 1
            fitscore = test_func(x, N)
            x.fitness = fitscore[2]
            popscorelist.append(x.fitness)
            if x.fitness <= popbestscore:
                popbestscore = x.fitness
                bestinrun = x

        yaxis.append(popbestscore)

        avgpopscore = statistics.mean(popscorelist)
        avgscorelist.append(avgpopscore)
        generation = []
        generation.append(currentrun)

        xaxis.append(genz)
        print("in generation: ", currentrun,
              " avg best fitness is: ", popbestscore)

        # plt.plot(gen, label="Test")
        if currentrun == runs - 1:
            bestrunfinal.append(popbestscore)
            avgrunfinal.append(avgpopscore)
            plt.plot(yaxis, label="muterate:" + str(mutrate) +
                     "Mutstep:" + str(mutstep) + "Best in gen 100: " +
                     "{:10.3f}".format(popbestscore))
            plt.plot(avgscorelist, label="muterate:" + str(mutrate) +
                     "Mutstep:" + str(mutstep) + "Average in gen 100: " +
                     "{:10.3f}".format(avgpopscore))

    # plt.show()

    return xaxis, yaxis, avgscorelist, bestrunfinal, avgrunfinal, bestinrun


bestrunfinal = []
avgrunfinal = []


newind = individual()
population = []
yaxis = np.array([])
avgaxis = np.array([])

mutrate = 0.0
noofmutrateincreases = 25
mutrateincrement = 0.005
mutstep = 0.0
noofmutstepincreases = 30
mutstepincrement = 0.15
startingmutrate = mutrate
startingmutstep = mutstep

numbertoavgover = int(input("Number of generation runs to average over: "))
runs = int(input("Enter the number of generations to run for: "))

GAsettings = {"Starting mutrate: ": startingmutrate, "Starting mutstep": startingmutstep, "Number of runs to average over": numbertoavgover,
              "No of mutstep increases": noofmutstepincreases, "No of mutrate increases": noofmutrateincreases, "Size of mutrate increases": mutrateincrement, "Size of mutstep": mutstepincrement, "Number of generations": runs}

bestofrun = []
listofaverage = []

count = 0
totalfitpop = 0
start = time.time()
for a in range(noofmutstepincreases):
    mutstep += mutstepincrement
    mutrate = startingmutrate
    for z in range(noofmutrateincreases):
        mutrate += mutrateincrement
        for x in range(numbertoavgover):
            population = pop_init()
            fitscore = test_func(population[0], N)
            popbestscore = fitscore[2]
            for currentrun in range(0, runs):
                popscorelist = []
                avgpopscore = []
                counter = -1
                for x in population:
                    fitscore = test_func(x, N)
                    x.fitness = fitscore[2]
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
                                if gene > 10:
                                    gene = 10
                            else:
                                gene -= mutstep
                                if gene < -10:
                                    gene = -10
                        newind.gene.append(gene)
                    mutatedgenes.append(newind)

                for x in mutatedgenes:
                    fitscore = test_func(x, N)
                    x.fitness = fitscore[2]

                worsebaby = mutatedgenes[0]
                bestbaby = mutatedgenes[0]
                for x in mutatedgenes:
                    if x.fitness < bestbaby.fitness:
                        bestbaby = x

                for x in mutatedgenes:
                    if x.fitness > worsebaby.fitness:
                        worsebaby = x
                indexno = mutatedgenes.index(worsebaby)
                mutatedgenes[0] = bestbaby
                population = copy.deepcopy(mutatedgenes)

                counter = -1
                for x in population:
                    fitscore = test_func(x, N)
                    x.fitness = fitscore[2]

                for x in population:
                    popscorelist.append(x.fitness)
                    if x.fitness <= popbestscore:
                        popbestscore = x.fitness

                yaxis = np.append(yaxis, popbestscore)

                avgpopscore = statistics.mean(popscorelist)
                count += 1
                print(count)

                # print(currentrun, popbestscore)
            bestofrun.append(popbestscore)
            if len(bestofrun) == numbertoavgover:
                averageofruns = statistics.mean(bestofrun)
                print("avg:", averageofruns)
                bestofrun.clear()
                print("Still going...")
                print(avgpopscore)
                listofaverage.append(
                    ["{:10.3f}".format(mutrate), "{:10.3f}".format(mutstep), float(averageofruns), float(avgpopscore)])


end = time.time()
elapsed = end - start

sortedlist = sorted(listofaverage, key=lambda x: x[2])
# sortedlist = npversion[np.argsort(npversion[:, 2])]
currentbest = sortedlist[0]
for x in sortedlist:
    if x[2] < sortedlist[0][2]:
        currentbest = x
table = tabulate(listofaverage, headers=[
                 "Mutrate", "Mutstep", "Best Fitness", "Avg Fitness of gen 100"], tablefmt="pretty")

# sortedlist = npversion[npversion[:, 2].argsort()]
tablesorted = tabulate(sortedlist, headers=[
                       "Mutrate", "Mutstep", "Best Fitness", "Avg Fitness of gen 100"], showindex="always", tablefmt="pretty")
print(tablesorted)

print("BEST:\nMutstep:" +
      str(currentbest[0]) + "Mutrate:" + str(currentbest[1]) + "Score:" + str(currentbest[2]))

topperformers = []
for i in range(10):
    topperformers.append(sortedlist[i])

toptable = tabulate(topperformers, headers=[
    "Index", "Mutrate", "Mutstep", "Best Fitness"], showindex="always", tablefmt="pretty")

f = open(
    "/Users/ashleypearson/Documents/UWE/Year Two/AI2/Assignment/runresults.txt", "w")
f.write("-----------------GA Results-----------------\nSettings as follows:\n")
f.write(json.dumps(GAsettings) + "\n")
f.write("Unsorted data:\n" + table + "\n")
f.write("Sorted table: \n" + tablesorted + "\n")
f.write(str(currentbest) + "\nTime to run: " +
        str(elapsed / 60) + " minutes")
f.write("\nTop 10 performers to further investigate: \n" + toptable + "\n")

finalresults = []
for x in topperformers:
    toptenrun = scoreplotter(N, P, test_func, float(x[0]), float(x[1]))
    avgoftenavgs = statistics.mean(avgrunfinal)
    avgoftenbests = statistics.mean(bestrunfinal)
    finalresults.append([x[0], x[1], avgoftenbests, avgoftenavgs])

finalresultstable = tabulate(finalresults, headers=[
    "Index", "Mutrate", "Mutstep", "best fitness at gen100 (10runs)", "avg fitness at gen100(10runs)"], showindex="always", tablefmt="pretty")
print(finalresultstable)
f.write("\nFinal Results of running the 10 best discovered combinations for 10 runs and averaging average fitness and best fitness in generation 100\n " + finalresultstable)
plt.legend()
plt.xlabel('Generations Ran')
plt.ylabel("Fitness")
plt.title("Fitness (Best and Average) of 10 best performers")
plt.show()


randomind = individual()
population = []
tempgene = []
for y in range(0, N):
    tempgene.append(random.uniform(-10, 10))
randomind.gene = tempgene.copy()

run = test_func(toptenrun[5], N)
runrandom = test_func(randomind, N)

fig = plt.figure()

for x in range(3):
    randomind = individual()
    population = []
    tempgene = []
    for y in range(0, N):
        rando = random.uniform(-10, 10)
        tempgene.append(rando)
        print(rando)
    randomind.gene = tempgene.copy()
    xaxis = []
    for x in range(1, 20):
        xaxis.append(randomind.gene[x])
    runrandom = test_func(randomind, N)
    print(len(xaxis), len(runrandom[0]))
    plt.scatter(xaxis, runrandom[0], label=(
        "Random individual number: " + str(x) + "Total Ind fitness: " + "{:10.3f}".format(runrandom[1])))
xaxis = []
for x in range(1, 20):
    xaxis.append(toptenrun[5].gene[x])
yaxis = run
runtotal = []
randomtotal = []
for x in range(len(xaxis)):
    runtotal.append([toptenrun[5].gene[x], run[0][x]])
    randomtotal.append([randomind.gene[x], runrandom[0][x]])
print(runtotal)
print(len(runtotal))
runtotal = tabulate(runtotal, headers=("Good genes", "Fitness"))
print(runtotal)

plt.scatter(xaxis, run[0], marker='s', c='black',
            label="Top performer total fitness: " + "{:10.3f}".format(run[1]))
plt.ticklabel_format(style="plain")
plt.legend()
plt.ylabel("Fitness")
plt.xlabel("Individual gene value")
plt.title("Plot of individual genes and corresponding fitness value")
plt.show()

f.close()
