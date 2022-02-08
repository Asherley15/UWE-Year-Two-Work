
# Imports required, plotting tools, numpy for efficient array sorting,tabulate for prettyprinting of data and json for packaging of data.
from typing import Counter
from matplotlib import pyplot as plt
import random
import numpy as np
import copy
import statistics
from numpy.core.numeric import cross
from numpy.lib.function_base import select
from tabulate import *
import json
import time

# Define test function for use in application.


# def test_func(ind, N):
#     fitness = 0
#     for x in range(N):

#         return fitness += (ind.gene[x] - ind.gene)**2+

def selection(population, P, offspring):

    for i in range(0, P):
        parent1 = random.randint(0, P - 1)
        off1 = population[parent1]
        parent2 = random.randint(0, P - 1)
        off2 = population[parent2]
        if off1.fitness > off2.fitness:
            offspring.append(off2)

        else:
            offspring.append(off1)
        for x in offspring:
            x.fitness = test_func(x, N)
    return offspring


def test_func(ind, N):
    fitness = 0
    for x in range(N):
        fitness += (ind.gene[x]**4 - 16 * ind.gene[x]**2 + 5 * ind.gene[x])
    return fitness / 2


# Define an inidividual with a length of N and an initial fitness of 0.
class individual:
    def __init__(self):
        self.gene = [0] * N
        self.fitness = 0


# Declare N(length) and P (generation size)
N = 20
P = 50

# Set the decimal place accuracy of NP arrays and suppress scientific notation for easier readibility.
np.set_printoptions(precision=5, suppress=True)

# Score plotter function which takes the best mutsteps and mutrates discovered in the main program and plots them to a graph after running each individually for 100 generations


def elitism(mutatedgenes):
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
    return mutatedgenes


def mutation(offspring, mutatedgenes):
    for i in range(0, P):
        newind = individual()
        newind.gene = []
        for j in range(0, N):
            mutprob = random.random()
            gene = offspring[i].gene[j]
            if (mutprob) < (mutrate):
                if random.random() < 0.5:
                    gene += mutstep
                    if gene > 5.12:
                        gene = 5.12
                else:
                    gene -= mutstep
                    if gene < -5.12:
                        gene = -5.12
            newind.gene.append(gene)
        mutatedgenes.append(newind)
        for x in mutatedgenes:
            x.fitness = test_func(x, N)
    return mutatedgenes


def crossover(offspring):
    crosspoint = random.randint(0, N - 1)
    for i in range(0, P, 2):

        tempgene = offspring[i].gene.copy()

        for k in range(0, crosspoint):
            offspring[i].gene[k] = offspring[i + 1].gene[k]
            offspring[i + 1].gene[k] = tempgene[k]
    return offspring


def scoreplotter(N, P, test_func, mutrate, mutstep):
    # Empty array to hold average score.
    avgscorelist = []
    # Create empty population array
    population = []
    # Create array for which the best score of each gen is appended to,
    yaxis = []
# Loop through size of P and create individuals with individual Genes- N with random values within upper and lower range.
    for gen in range(0, P):
        tempgene = []
        for y in range(0, N):
            tempgene.append(random.uniform(-5, 5))
        newind = individual()
        newind.gene = tempgene.copy()
        population.append(newind)
# Set generations in a run to 100
    runs = 100
    # Initialise popbest score to the first individual to set a default value.
    popbestscore = test_func(population[0], N)
# For loop to run through desired generations, with current run declared for easy visilbity of current progress.
    for currentrun in range(0, runs):
        # declare empty array to hold every score in a generation.
        popscorelist = []
# Assign individuals fitness values.
        for x in population:
            x.fitness = test_func(x, N)
        offspring = []
        selection(population, P, offspring)
        crossover(offspring)
        mutatedgenes = []
        mutation(offspring, mutatedgenes)
        elitism(mutatedgenes)
        population = copy.deepcopy(mutatedgenes)
        for x in population:
            x.fitness = test_func(x, N)
            popscorelist.append(x.fitness)
            if x.fitness <= popbestscore:
                popbestscore = x.fitness
        yaxis.append(popbestscore)
        avgpopscore = statistics.mean(popscorelist)
        print(avgpopscore)
        avgscorelist.append(avgpopscore)
        generation = []
        generation.append(currentrun)

        # plt.plot(gen, label="Test")
        if currentrun == runs - 1:
            plt.plot(yaxis, label="Best in gen -- muterate: " + str(mutrate) +
                     "Mutstep: " + str(mutstep) + "{:10.3f}".format(popbestscore))
            plt.plot(avgscorelist, label="Average in gen -- muterate: " + str(mutrate) +
                     "Mutstep: " + str(mutstep) + "{:10.3f}".format(avgpopscore))

    # plt.show()

    return yaxis, avgscorelist


newind = individual()
population = []
yaxis = []
avgaxis = np.array([])
# usercheck = input("Do you wish to manually adjust GA settings? Y/N")
# print(usercheck)
# if (usercheck in ['Y', 'y', 'YES', 'yes', 'Yes']):
#     mutrate = float(input("Enter starting Mutrate as a float: "))
#     noofmutrateincreases = int(input("Enter No of Mutrate increments:"))
#     mutrateincrement = float(
#         input("Enter the value of each Mutrate increment: "))
#     mutstep = float(input("Enter starting Mutstep as a float: "))
#     noofmutstepincreases = int(input("Enter No of Mutstep increments:"))
#     mutstepincrement = float(
#         input("Enter the value of each Mutstep increment: "))
# else:
mutrate = 0
noofmutrateincreases = 15
mutrateincrement = 0.01
mutstep = 0
noofmutstepincreases = 10
mutstepincrement = 0.2


startingmutrate = mutrate
startingmutstep = mutstep
numbertoavgover = int(input("Number of generation runs to average over: "))
runs = int(input("Enter the number of generations to run for: "))
printcheck = input("Do you wish to save this run to text file?: Y/N ")

GAsettings = {"Starting mutrate: ": startingmutrate, "Starting mutstep": startingmutstep, "Number of runs to average over": numbertoavgover,
              "No of mutstep increases": noofmutstepincreases, "No of mutrate increases": noofmutrateincreases, "Size of mutrate increases": mutrateincrement, "Size of mutstep increments": mutstepincrement, "Number of generations": runs}

listofaverage = []
bestofrun = []
run = 0
count = 0
totalfitpop = 0
avgscorelist = []
start = time.time()
for a in range(noofmutstepincreases):
    mutstep += mutstepincrement
    mutrate = startingmutrate
    for z in range(noofmutrateincreases):
        mutrate += mutrateincrement
        for x in range(numbertoavgover):
            population = []
            for gen in range(0, P):
                tempgene = []
                for y in range(0, N):
                    tempgene.append(random.uniform(-5, 5))
                newind = individual()
                newind.gene = tempgene.copy()
                population.append(newind)
                popbestscore = test_func(population[0], N)
                averageoflastpop = []
            for currentrun in range(0, runs):

                popscorelist = []
                offspring = []
                selection(population, P, offspring)
                crossover(offspring)
                mutatedgenes = []
                mutation(offspring, mutatedgenes)
                elitism(mutatedgenes)

            population = copy.deepcopy(mutatedgenes)
            for x in population:
                x.fitness = test_func(x, N)
                popscorelist.append(x.fitness)
                if x.fitness <= popbestscore:
                    popbestscore = x.fitness
            count += 1

            yaxis.append(popbestscore)
            avgpopscore = statistics.mean(popscorelist)
            print(avgpopscore)
            avgscorelist.append(avgpopscore)
            generation = []
            generation.append(currentrun)

            yaxis.append(popbestscore)

            avgpopscore = statistics.mean(popscorelist)
            avgscorelist.append(avgpopscore)
            if currentrun == runs - 1:
                averageoflastpop.append(avgpopscore)
            print(count)
            bestofrun.append(popbestscore)

            if len(bestofrun) == numbertoavgover:
                averageofruns = statistics.mean(bestofrun)
                finalaverages = statistics.mean(averageoflastpop)
                bestofrun.clear()
                listofaverage.append(
                    ["{:10.3f}".format(mutrate), "{:10.3f}".format(mutstep), averageofruns, finalaverages])
end = time.time()
elapsed = end - start
npversion = np.array(listofaverage)
table = tabulate(npversion, headers=[
    "Index", "Mutrate", "Mutstep", "Best Fitness of last gen(avg)", "Average of last generation(avg)"], showindex="always", tablefmt="pretty")
print(table)
currentbest = listofaverage[0]
for x in listofaverage:
    if x[2] < currentbest[2]:
        currentbest = x
print("BEST:\nMutstep:" +
      str(currentbest[0]) + "Mutrate:" + str(currentbest[1]) + "Score:" + str(currentbest[2]))
sorted = npversion[npversion[:, 2].argsort()]
reversed = np.flipud(sorted)
tablesorted = tabulate(reversed, headers=[
    "Index", "Mutrate", "Mutstep", "Best Fitness"], showindex="always", tablefmt="pretty")
print(tablesorted)

print("BEST:\nMutstep:" +
      str(currentbest[0]) + "Mutrate:" + str(currentbest[1]) + "Score:" + str(currentbest[2]))

topperformers = []
for i in range(10):
    bestperformerno = i + 1
    topperformers.append(reversed[i])

toptable = tabulate(topperformers, headers=[
    "Index", "Mutrate", "Mutstep", "Best Fitness"], showindex="always", tablefmt="pretty")
print(toptable)
if printcheck == "Y" or "y" or "yes":
    f = open(
        "/Users/ashleypearson/Documents/UWE/Year Two/AI2/Assignment/runresults.txt", "w")
    f.write("-----------------GA Results-----------------\nSettings as follows:\n")
    f.write(json.dumps(GAsettings) + "\n")
    f.write("Unsorted data:\n" + table + "\n")
    f.write("Sorted table: \n" + tablesorted + "\n")
    f.write(str(currentbest) + "\nTime to run: " +
            str(elapsed / 60) + " minutes")
    f.write("\nTop 10'%' of performers to further investigate: \n" + toptable + "\n")
    f.close()


for x in topperformers:
    scoreplotter(N, P, test_func, float(x[0]), float(x[1]))
plt.legend()
plt.xlabel('Generations Ran')
plt.ylabel("Fitness")
plt.title("Fitness (Best and Average) of " +
          str(bestperformerno) + " best performers")
plt.show()
