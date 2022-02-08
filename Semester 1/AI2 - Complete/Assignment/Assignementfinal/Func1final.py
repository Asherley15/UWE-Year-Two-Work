from typing import final
import matplotlib
from matplotlib import pyplot as plt
import random
import numpy as np
import copy
import statistics
from numpy.core.fromnumeric import size, sort
from tabulate import *
import json
import time


# Defining individual class


class individual:
    def __init__(self):
        self.gene = [0] * N
        self.fitness = 0


# Declare N(individual gene length) and P(Population size)
N = 20
P = 150

################ ADJUSTABLE MUTRATE/MUTSTEP SETTINGS ################
mutrate = 0.0
noofmutrateincreases = 20
mutrateincrement = 0.005
mutstep = 0.0
noofmutstepincreases = 20
mutstepincrement = 0.1
startingmutrate = mutrate
startingmutstep = mutstep
startingP = P

################ ADJUSTABLE MUTRATE/MUTSTEP SETTINGS ################

# Best of run holds the best score from a full run of the GA (100 generations for example.)
bestofrun = []
# avgofavgs holds a populations average score at the end of a run.
avgofavgs = []
# List of average is a 2-d array that holds the mutstep,mutrate average of best scores and average population scores after numerous runs.
listofaverage = []

# Set  numpy to 5 decimal places and supress scientific notation for readibility in tables.
np.set_printoptions(precision=5, suppress=True)

# Define test function


def test_func(ind, N):
    # Set fitness initially to 0.
    fitness = 0
    # Calculate total fitness of an individual.
    fitnesstotal = 0
    # Score individual fitness scores in an array.
    fitnessarray = []
    # Loop through an inidividuals length.
    for i in range(N):
        # Dixon-Price fitness function
        fitness = (ind.gene[i]**4 - 16 * ind.gene[i]**2 + 5 * ind.gene[i])
        fitness = fitness / 2
        fitnessarray.append(fitness)
    # Append individual fitnesses to an array.
    fitnesstotal = sum(fitnessarray)
    return fitness, fitnessarray, fitnesstotal


# define function that takes the best ten results from the wide parameter sweep, with the settings that produced those scores.


def scoreplotter(N, P, test_func, mutrate, mutstep, runs):
    # array to hold the average scores of a population
    avgscorelist = []
    # Array to hold a population of individuals
    population = []
    # Array to hold best score in a generation.
    yaxis = []

# Loop through population
    for x in range(0, P):
        # Create array to hold individiual gene values
        tempgene = []
        # Loop through genes in an individual
        for y in range(0, N):
            # Add a gene between of a value between -5 and 5 (x)
            tempgene.append(random.uniform(-5, 5))
            # Create an individual called new ind
        newind = individual()
        # Assign newind the genes created in the above loop.
        newind.gene = tempgene.copy()
        # Add the indiviudal to the population, continue until x=P
        population.append(newind)

    xaxis = []
    genz = 0
# Initialise popbestscore to the first individual in the population.
    fitscore = test_func(population[0], N)
    popbestscore = fitscore[2]
# Loop until the specified number of generations.
    for currentrun in range(0, runs):
        popscorelist = []
        genz += 1
# Loop through the population and assign a fitness score to each individual.
        for x in population:
            fitscore = test_func(x, N)
            x.fitness = fitscore[2]
# Create an array to contain offspring chosen from tournament selection.
        offspring = []
        # Loop through population, selecting and copying the
        for i in range(0, P):
            # create a copy of two random individuals
            parent1 = random.randint(0, P - 1)
            off1 = population[parent1]
            parent2 = random.randint(0, P - 1)
            off2 = population[parent2]
            # Check which copy has the better fitness and append to the new offspring array.
            if off1.fitness > off2.fitness:
                offspring.append(off2)
            else:
                offspring.append(off1)
# Loop through population in steps of 2 and select a crosspoint.
        for i in range(0, P, 2):
            crosspoint = random.randint(0, N - 1)
# Create a copy of an individual.
            tempgene = offspring[i].gene.copy()
# Loop through the genes of an indiviual up to the crosspoint and swap the genes  between individual i and i+1
            for k in range(0, crosspoint):
                offspring[i].gene[k] = offspring[i + 1].gene[k]
                offspring[i + 1].gene[k] = tempgene[k]
# Create an array to hold mutated genes.
        mutatedgenes = []
        for i in range(0, P):
            # Create an individual with an empty gene array.
            newind = individual()
            newind.gene = []
            # Loop through an indiviudals array of genes
            for j in range(0, N):
                mutprob = random.random()
                gene = offspring[i].gene[j]
                # pick a value between 0 and mutstep to alter the gene by.
                alter = abs(random.uniform(0, mutstep))
                # If random number between 0-1 is smaller than mutrate there is a 50% chance for the gene to have the alter rate added.
                if (mutprob) < (mutrate):
                    if random.random() < 0.5:
                        gene += alter
                        if gene > 5:
                            gene = 5
                    else:
                        # If random number between 0-1 is larger than mutrate there is a 50% chance for the gene to have the alter rate subtracted.
                        gene -= alter
                        if gene < -5:
                            gene = -5
                # Append the gene, altered or not the the new individual and then to the mutated genes array.
                newind.gene.append(gene)
            mutatedgenes.append(newind)
# Loop through mutated genes and assign fitness scores.
        for x in mutatedgenes:
            fitscore = test_func(x, N)
            x.fitness = fitscore[2]
# Set both the worst individual and best individual to individual 0 so a value is assigned.
        worsebaby = mutatedgenes[0]
        bestbaby = mutatedgenes[0]
# Loop through mutated genes until both the best and worst individuals have been found
        for x in mutatedgenes:
            if x.fitness < bestbaby.fitness:
                bestbaby = x
            if x.fitness > worsebaby.fitness:
                worsebaby = x
        # Get the index number of the worst individual in the array.
        indexno = mutatedgenes.index(worsebaby)
        # Replace the worst individual in the population
        mutatedgenes[indexno] = bestbaby
        # Make population a copy of the newly created mutated genes array.
        population = copy.deepcopy(mutatedgenes)
# Loop through population setting indiivdual fitness scores.
        for x in population:
            fitscore = test_func(x, N)
            x.fitness = fitscore[2]
            # Add fitness scores to popscorelist array.
            popscorelist.append(x.fitness)
            # Loop through the array finding the best score.
            if x.fitness <= popbestscore:
                popbestscore = x.fitness
                # Set a copy of the best individual to bestinrun.
                bestinrun = x
# Append popbestscore to array
        yaxis.append(popbestscore)
# Calculate the average fitness in a population.
        avgpopscore = statistics.mean(popscorelist)
# Append average score to an array containing average scores of each generation
        avgscorelist.append(avgpopscore)
        # Append the current run to the xaxis.
        xaxis.append(currentrun)
# If the run == the last run of the GA:
        if currentrun == runs - 1:
            # Store final best score and avg of population of the run.
            bestrunfinal = popbestscore
            avgrunfinal = avgpopscore
            # Plot best scores and average scores to the graph of best performers.
            plt.plot(yaxis, label="muterate:" + str(mutrate) +
                     "Mutstep:" + str(mutstep) + "Best in gen 100: " +
                     "{:10.3f}".format(popbestscore))
            plt.plot(avgscorelist, label="muterate:" + str(mutrate) +
                     "Mutstep:" + str(mutstep) + "Average in gen 100: " +
                     "{:10.3f}".format(avgpopscore))

    return xaxis, yaxis, avgscorelist, bestrunfinal, avgrunfinal, bestinrun


# Get the number of complete runs to average over
numbertoavgover = int(input("Number of generation runs to average over: "))

# Get the number of generations per run to complete.
runs = int(input("Enter the number of generations to run for: "))
startingruns = runs
# Store the settings of the run in a dictionary to be printed to file later.
GAsettings = {"Starting mutrate: ": startingmutrate, "Starting mutstep": startingmutstep, "Number of runs to average over": numbertoavgover,
              "No of mutstep increases": noofmutstepincreases, "No of mutrate increases": noofmutrateincreases, "Size of mutrate increases": mutrateincrement, "Size of mutstep": mutstepincrement, "Number of generations": runs}

# Start a timer
start = time.time()
# Set a progresser counter to 0 to be incremented on each generation.
progresscounter = 0
# Set total number of runs to allow for visual progress check on larger runs.
totalruns = (noofmutrateincreases * noofmutstepincreases *
             numbertoavgover * runs)

# Loop through number of mutstep increases
for a in range(noofmutstepincreases):
    # increment mutstep value
    mutstep += mutstepincrement
    # each time inner loop returns to here, reset mutrate to starting mutrate.
    mutrate = startingmutrate
    # Loop through mutrate increases
    for z in range(noofmutrateincreases):
        # increment mutrate value
        mutrate += mutrateincrement
        # Complete each of the parameter combinations 'numbertoavgover' times.
        for x in range(numbertoavgover):
            population = []
            # Population initialisation.
            for gen in range(0, P):
                tempgene = []
                for y in range(0, N):
                    tempgene.append(random.uniform(-5, 5))
                newind = individual()
                newind.gene = tempgene.copy()
                population.append(newind)
            # Set popbestscore.
            fitscore = test_func(population[0], N)
            popbestscore = fitscore[2]
            # Loop through runs
            for currentrun in range(0, runs):
                popscorelist = []
                avgpopscore = []
                for x in population:
                    fitscore = test_func(x, N)
                    x.fitness = fitscore[2]

                # Selection
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
                # Crossover
                crosspoint = random.randint(0, N - 1)
                for i in range(0, P, 2):
                    tempgene = offspring[i].gene.copy()
                    for k in range(0, crosspoint):
                        offspring[i].gene[k] = offspring[i + 1].gene[k]
                        offspring[i + 1].gene[k] = tempgene[k]

                # Mutation
                mutatedgenes = []
                for i in range(0, P):
                    newind = individual()
                    newind.gene = []
                    for j in range(0, N):
                        mutprob = random.random()
                        gene = offspring[i].gene[j]
                        alter = abs(random.uniform(0, mutstep))
                        if (mutprob) < (mutrate):
                            if random.random() < 0.5:
                                gene += alter
                                if gene > 5:
                                    gene = 5
                            else:
                                gene -= alter
                                if gene < -5:
                                    gene = -5
                        newind.gene.append(gene)
                    mutatedgenes.append(newind)
                # Assign fitness values
                for x in mutatedgenes:
                    fitscore = test_func(x, N)
                    x.fitness = fitscore[2]

                # Elitism
                worsebaby = mutatedgenes[0]
                bestbaby = mutatedgenes[0]
                for x in mutatedgenes:
                    if x.fitness < bestbaby.fitness:
                        bestbaby = x
                    if x.fitness > worsebaby.fitness:
                        worsebaby = x
                indexno = mutatedgenes.index(worsebaby)
                mutatedgenes[indexno] = bestbaby
                population = copy.deepcopy(mutatedgenes)

                # Assign fitness scores
                for x in population:
                    fitscore = test_func(x, N)
                    x.fitness = fitscore[2]
                    popscorelist.append(x.fitness)
                    if x.fitness <= popbestscore:
                        popbestscore = x.fitness
                # Calculate average population score
                avgpopscore = statistics.mean(popscorelist)
                # Print progress.
                progresscounter += 1
                print(progresscounter, "/", totalruns)
            # Append best score to an array.
            bestofrun.append(popbestscore)
            avgofavgs = statistics.mean(popscorelist)
            # If number of final popbestscores recorded == number to avg over:
            if len(bestofrun) == numbertoavgover:
                # Calculate an average of best final scores
                averageofruns = statistics.mean(bestofrun)
                # Clear bestofrun for next parameter run
                bestofrun.clear()
                # Append mutrate, mutstep, average of best scores and
                listofaverage.append(
                    ["{:10.3f}".format(mutrate), "{:10.3f}".format(mutstep), float(averageofruns), float(avgofavgs)])
# End timer
end = time.time()
elapsed = end - start

# created sorted list sorted on index 2 of list of average(averageofruns)
sortedlist = sorted(listofaverage, key=lambda x: x[2])

# Set current best to the first in loop and then loop through bests to find the true best
currentbest = sortedlist[0]
for x in sortedlist:
    if x[2] < sortedlist[0][2]:
        currentbest = x
# Create a table of the bests
table = tabulate(listofaverage, headers=["Index",
                 "Mutrate", "Mutstep", "Best Fitness", "Avg Fitness of gen 100"], showindex="always", tablefmt="pretty")
# Create a table of the list sorted based on best score achieved.
tablesorted = tabulate(sortedlist, headers=["Index",
                       "Mutrate", "Mutstep", "Best Fitness", "Avg Fitness of gen 100"], showindex="always", tablefmt="pretty")
# Create an array to hold the best 5 performers from the sorted list.
topperformers = []
for i in range(5):
    topperformers.append(sortedlist[i])
# Create a table of the best 5 performers.
toptable = tabulate(topperformers, headers=[
    "Index", "Mutrate", "Mutstep", "Best Fitness"], showindex="always", tablefmt="pretty")

# Create an array to hold the results of running the top 5 performers.
finalresults = []
p = 0
for x in topperformers:
    # Pass in N,P, test function and the mutrate and number of runs to run.
    toptenrun = scoreplotter(N, P, test_func, float(x[0]), float(x[1]), runs)
    if p == 0:
        best = toptenrun[5]
    # Record the avg population score.
    avgs = toptenrun[4]
    # Record the best recorded score.
    bests = toptenrun[3]
    # Append the results and mutrate, mutstep to an array.
    finalresults.append([x[0], x[1], bests, avgs])
    p += 1
# Sort the final results array and create a table.
finalresults = sorted(finalresults, key=lambda x: x[2])
finalresultstable = tabulate(finalresults, headers=[
    "Index", "Mutrate", "Mutstep", "best fitness", "avg fitness"], showindex="always", tablefmt="pretty")


# Open/Create a text file and print GA settings, all 4 tables, time to complete, and the best final performer before closing the file.
f = open(
    "/Users/ashleypearson/Documents/UWE/Year Two/AI2/Assignment/Testresults/runresults.txt", "w")
f.write("-----------------GA Results-----------------\nSettings as follows:\n")
f.write(json.dumps(GAsettings) + "\n")
f.write("Unsorted data:\n" + table + "\n")
f.write("Sorted table: \n" + tablesorted + "\n")
f.write("\nTop 10 performers to further investigate: \n" + toptable + "\n")
f.write("\nFinal Results of running the 5 best discovered combinations for 5 runs and averaging average fitness and best fitness in generation " +
        str(runs) + "\n" + finalresultstable)
f.write("\nTime to run: " +
        str(elapsed / 60) + " minutes")
f.write("\nBest performer is:" + "\nMutrate:" +
        str(finalresults[0][0]) + "\nMutstep:" + str(finalresults[0][1]) + "\nBest score: " + str(finalresults[0][2]) + "\nAverage score: " + str(finalresults[0][3]))
# Close the file.


# Plot the 5 best performers on a graph, and show it.
plt.legend()
plt.xlabel('Generations Ran')
plt.ylabel("Fitness")
plt.title("Fitness (Best and Average) of 5 best performers")
plt.show()

# Create a scatter graph
fig = plt.figure()
# Create 3 random individuals with random genes
for x in range(3):
    randomind = individual()
    population = []
    tempgene = []
    for y in range(0, N):
        rando = random.uniform(-5, 5)
        tempgene.append(rando)
    randomind.gene = tempgene.copy()
    # Add the individual genes to a new Xaxis array.
    xaxis = []
    for x in range(0, 20):
        xaxis.append(randomind.gene[x])
    # Get the fitness scores for individual genes
    runrandom = test_func(randomind, N)
    # Plot the individiual gene values, and fitness scores on a scatter graph.
    plt.scatter(xaxis, runrandom[1], label=(
        "Random individual number " + "Total Ind fitness: " + "{:10.3f}".format(runrandom[2])))
# Create a new x acis array
xaxis = []
# add the individual gene values of the best discovered individual to an array.
for x in range(0, 20):
    xaxis.append(toptenrun[5].gene[x])
# get the fitness values of best individual genes.
run = test_func(best, N)

# Plot the best performer on the above scatter with Black Squares as the icon to make for consistent, easy comparison.
plt.scatter(xaxis, run[1], marker='s', c='black',
            label="Top performer total fitness: " + "{:10.3f}".format(run[2]))
# Format scatter as desired with correct labels and styles.
plt.ticklabel_format(style="plain")
plt.legend()
plt.ylabel("Fitness")
plt.xlabel("Individual gene value")
plt.title("Plot of individual genes and corresponding fitness value")
plt.show()

best0 = []
average0 = []
# Run the best individual 3 times with a fixed population and generation number and plot to a graph to show multiple runs
for x in range(3):
    run = scoreplotter(N, P, test_func, float(
        finalresults[0][0]), float(finalresults[0][1]), runs)
    # Save the best scores and averages scores from each run to an array.
    best0.append([run[1]])
    average0.append([run[2]])

# Calculate and plot averages of bests and averages to the same graph.
# (Method of calculating mean taken from StackOverflow user - Saullo G. P. Castro, Initial code available below:)
# https://stackoverflow.com/questions/18461623/average-values-in-two-numpy-arrays/18461943
bests = np.mean(np.array([best0[0], best0[1], best0[2]]), axis=0)
plt.plot(bests[0], '--', label="Average of Bests")
avgs = np.mean(np.array([average0[0], average0[1], average0[2]]), axis=0)
plt.plot(avgs[0], '--', label="Average of Averages")

plt.legend()
plt.xlabel('Generations Ran')
plt.ylabel("Fitness")
plt.title("Fitness (Best and Average) of 5 runs of best performer")
plt.show()

scorelist = []
runs = 0
# Create a nested loop that runs th best performer found from the above searches with an incrementing number of population members and generations.
counter = 0
for x in range(5):
    runs += 100
    P = startingP
    for j in range(5):
        counter += 1
        print(str(counter) + "/" + str((5 * 5)))
        score = scoreplotter(N, P, test_func, float(
            finalresults[0][0]), float(finalresults[0][1]), runs)
        scorelist.append([runs, P, score[3], score[4]])
        P += 50
scorelist = tabulate(scorelist, headers=[
    "Runs", "Pop Size", "Best", "Average"], tablefmt="pretty")
print(scorelist)
f.write("\n" + scorelist)

f.close()
