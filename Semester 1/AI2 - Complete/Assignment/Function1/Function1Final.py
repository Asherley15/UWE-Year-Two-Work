from matplotlib import pyplot as plt
import random
import numpy as np
import copy
import statistics
import math
from numpy.core.fromnumeric import argsort
from tabulate import *
import json
import time

global N, P
N = 20
P = 50


class individual:
    def __init__(self):
        self.gene = [0] * N
        self.fitness = 0


def pop_initialise(population):
    for gen in range(0, P):
        tempgene = []
        for y in range(0, N):
            tempgene.append(random.uniform(-5, 5))
        newind = individual()
        newind.gene = tempgene.copy()
        population.append(newind)
    return population


def test_func(ind, N):
    fitness = 0
    for x in range(N):
        fitness += (ind.gene[x]**4 - 16 * ind.gene[x]**2 + 5 * ind.gene[x])
    return fitness / 2


fitnessscore = []

bestofrun = []
popscorelist = []
avgscorelist = np.array([])
listofaverage = []
np.set_printoptions(precision=5, suppress=True)


def scoreplotter(N, P, test_func, mutrate, mutstep):

    popscorelist = []
    avgscorelist = []

    newind = individual()
    population = []
    yaxis = []
    population = (pop_initialise(population))

    xaxis = []
    totalfitpop = 0
    genz = 0
    runs = 100
    popbestscore = test_func(population[0], N)

    for currentrun in range(0, runs):
        popscorelist = []
        genz += 1
        counter = -1
        for x in population:
            counter += 1
            population[counter].fitness = test_func(x, N)

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
            offspring[counter].fitness = test_func(x, N)
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
                        if gene > 5:
                            gene = 5
                    else:
                        gene -= mutstep
                        if gene < -5:
                            gene = -5
                newind.gene.append(gene)
            mutatedgenes.append(newind)

        totalfitmut = 0
        counter = -1

        for x in mutatedgenes:
            counter += 1
            totalfitmut += test_func(x, N)

        worsebaby = mutatedgenes[0]
        bestbaby = mutatedgenes[0]
        for x in mutatedgenes:
            if x.fitness < bestbaby.fitness:
                bestbaby = x

        for x in mutatedgenes:
            if x.fitness > worsebaby.fitness:
                worsebaby = x
        indexno = mutatedgenes.index(worsebaby)
        mutatedgenes[indexno] = bestbaby
        fitnessscore.append(totalfitmut)
        population = copy.deepcopy(mutatedgenes)

        counter = -1
        for x in population:
            counter += 1
            population[counter].fitness = test_func(x, N)

        for x in population:
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
noofmutrateincreases = 10
mutrateincrement = 0.01
mutstep = 0.0
noofmutstepincreases = 20
mutstepincrement = 0.1


startingmutrate = mutrate
startingmutstep = mutstep
numbertoavgover = int(input("Number of generation runs to average over: "))
runs = int(input("Enter the number of generations to run for: "))
printcheck = input("Do you wish to save this run to text file?: Y/N ")

GAsettings = {"Starting mutrate: ": startingmutrate, "Starting mutstep": startingmutstep, "Number of runs to average over": numbertoavgover,
              "No of mutstep increases": noofmutstepincreases, "No of mutrate increases": noofmutrateincreases, "Size of mutrate increases": mutrateincrement, "Size of mutstep": mutstepincrement, "Number of generations": runs}


run = 0
count = 0
totalfitpop = 0
start = time.time()
for a in range(noofmutstepincreases):
    mutstep += mutstepincrement
    mutrate = startingmutrate
    for z in range(noofmutrateincreases):
        mutrate += mutrateincrement
        for x in range(numbertoavgover):
            run += 1
            population = (pop_initialise(population))

            popbestscore = test_func(population[0], N)
            print(population[0])
            for currentrun in range(0, runs):
                popscorelist = []

                counter = -1
                for x in population:
                    counter += 1
                    population[counter].fitness = test_func(x, N)
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
                                if gene > 5:
                                    gene = 5
                            else:
                                gene -= mutstep
                                if gene < -5:
                                    gene = -5
                        newind.gene.append(gene)
                    mutatedgenes.append(newind)

                totalfitmut = 0
                counter = -1

                worsebaby = mutatedgenes[0]
                bestbaby = mutatedgenes[0]
                for x in mutatedgenes:
                    if x.fitness < bestbaby.fitness:
                        bestbaby = x

                for x in mutatedgenes:
                    if x.fitness > worsebaby.fitness:
                        worsebaby = x
                indexno = mutatedgenes.index(worsebaby)
                mutatedgenes[indexno] = bestbaby
                fitnessscore.append(totalfitmut)
                population = copy.deepcopy(mutatedgenes)

                counter = -1
                for x in population:
                    counter += 1
                    population[counter].fitness = test_func(x, N)

                for x in population:
                    popscorelist.append(x.fitness)
                    if x.fitness <= popbestscore:
                        popbestscore = x.fitness

                yaxis = np.append(yaxis, popbestscore)

                avgpopscore = statistics.mean(popscorelist)
                avgscorelist = np.append(avgscorelist, avgpopscore)

                # print(currentrun, popbestscore)
            bestofrun.append(popbestscore)
            if len(bestofrun) == numbertoavgover:
                averageofruns = statistics.mean(bestofrun)
                print("avg:", averageofruns)
                bestofrun.clear()
                print("Still going...")
                listofaverage.append(
                    ["{:10.3f}".format(mutrate), "{:10.3f}".format(mutstep), averageofruns])
            count += 1
            print(count)
end = time.time()
elapsed = end - start

sortedlist = sorted(listofaverage, key=lambda x: x[2])

table = tabulate(listofaverage, headers=[
    "Index", "Mutrate", "Mutstep", "Best Fitness"], showindex="always", tablefmt="pretty")

currentbest = listofaverage[0]
for x in listofaverage:
    if x[2] < currentbest[2]:
        currentbest = x

# sorted = npversion[npversion[:, 2].argsort()]


tablesorted = tabulate(sortedlist, headers=[
    "Index", "Mutrate", "Mutstep", "Best Fitness"], showindex="always", tablefmt="pretty")
print(tablesorted)

print("BEST:\nMutstep:" +
      str(currentbest[0]) + "Mutrate:" + str(currentbest[1]) + "Score:" + str(currentbest[2]))

topperformers = []
for i in range(10):
    topperformers.append(sortedlist[i])

for x in topperformers:
    print("CHECK:", x)
toptable = tabulate(topperformers, headers=[
    "Index", "Mutrate", "Mutstep", "Best Fitness"], showindex="always", tablefmt="pretty")
if printcheck == "Y" or "y" or "yes":
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
    print(x[0])
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


def fitness_scatter_plotter(ind, N):
    fitness = 0
    fitnesstotal = 0
    fitnessarray = []
    for x in range(N):
        fitness = (ind.gene[x]**4 - 16 * ind.gene[x]**2 + 5 * ind.gene[x]) / 2
        fitnessarray.append(fitness)
        fitnesstotal += fitness
    return fitnessarray, fitnesstotal


randomind = individual()
population = []
tempgene = []

for y in range(0, N):
    tempgene.append(random.uniform(-5, 5))
randomind.gene = tempgene.copy()

run = fitness_scatter_plotter(toptenrun[5], N)
runrandom = fitness_scatter_plotter(randomind, N)

fig = plt.figure()

for x in range(3):
    randomind = individual()
    population = []
    tempgene = []
    for y in range(0, N):
        rando = random.uniform(-5, 5)
        tempgene.append(rando)
        print(rando)

    randomind.gene = tempgene.copy()
    xaxis = randomind.gene
    runrandom = fitness_scatter_plotter(randomind, N)
    plt.scatter(xaxis, runrandom[0], label=(
        "Random individual number: " + str(x) + "Total Ind fitness: " + "{:10.3f}".format(runrandom[1])))
xaxis = toptenrun[5].gene
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
plt.legend()
plt.ylabel("Fitness")
plt.xlabel("Individual gene value")
plt.title("Plot of individual genes and corresponding fitness value")
plt.show()

f.close()
