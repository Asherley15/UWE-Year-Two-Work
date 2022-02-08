
from matplotlib import pyplot as plt
import random
import numpy as np
import copy
import statistics

N = 50
P = 50
fitnessscore = []
totalfitmut = 0

popscorelist = []
avgscorelist = np.array([])
popbestscore = 0


class individual:
    def __init__(self):
        self.gene = [0] * N
        self.fitness = 0


newind = individual()
population = []
yaxis = np.array([])
avgaxis = np.array([])

for gen in range(0, P):
    tempgene = []
    for y in range(0, N):
        tempgene.append(random.randint(0, 1))
    newind = individual()
    newind.gene = tempgene.copy()
    population.append(newind)


def test_func(ind):
    fitness = 0
    for i in range(1, N, 2):
        fitness += i * (2 * ind.gene[i]**2 - ind.gene[i - 1])**2
    return fitness + ((ind.gene[0] - 1)**2)


xaxis = np.array([])
totalfitpop = 0
genz = 0
runs = 500


for gencheck in range(0, 6):
    if popbestscore != 50:
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
                offspring.append(off1)

            else:
                offspring.append(off2)
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
        mutrate = 0.011
        print("GENLEVEL:", mutrate)
        mutcheck = 0
        total = 0
        for i in range(0, P):
            newind = individual()
            newind.gene = []
            for j in range(0, N):
                mutprob = random.random()
                gene = offspring[i].gene[j]
                total += 1
                if (mutprob) < (mutrate):
                    if (gene == 1):
                        gene = 0
                    else:
                        gene = 1
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
            if x.fitness > bestbaby.fitness:
                bestbaby = x


# bestbaby=individual()      bestbaby=population[] for x in population if x >bestbaby bestbaby=x
# Inverse this to find worse and overwrite
        population = copy.deepcopy(mutatedgenes)

        worsebaby = individual()
        worsebaby = population[0]
        for x in population:
            if x.fitness < worsebaby.fitness:
                worsebaby = x
        worsebaby = bestbaby
        fitnessscore.append(totalfitmut)

        counter = -1
        for x in population:
            counter += 1
            population[counter].fitness = test_func(x)

        for x in population:
            popscorelist.append(x.fitness)
            if x.fitness >= popbestscore:
                popbestscore = x.fitness

        yaxis = np.append(yaxis, popbestscore)

        avgpopscore = statistics.mean(popscorelist)
        avgscorelist = np.append(avgscorelist, avgpopscore)
        generation = []
        generation.append(gencheck)

        xaxis = np.append(xaxis, [genz])
        plt.plot(xaxis, yaxis, avgscorelist)
    else:
        break

z = 0
counter = 0
for z in avgscorelist:
    counter += 1
    print("Generation: ", counter, "  avg:", z)
counter = 0
for z in popscorelist:
    counter += 1
    print("Generation: ", counter, "  best:", z)
plt.xlabel('Generations Ran')
plt.ylabel("Fitness")
plt.title("Fitness (Best and Average)")

plt.show()
