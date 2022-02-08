from hashlib import new
from matplotlib import pyplot as plt
import random
import numpy as np

N = 10
P = 50


class individual:
    def __init__(self):
        gene = [] * N
        fitness = 0


population = []

for x in range(0, P):
    tempgene = []
    for y in range(0, N):
        tempgene.append(random.randint(0, 1))
    newind = individual()
    newind.gene = tempgene.copy()
    population.append(newind)


def test_func(ind):
    fitness = 0
    for x in range(N):
        fitness = fitness + ind.gene[x]
    return fitness


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
print("Parent values: ", totalfitpop)
print("Offspring values: ", totalfitoff)
if totalfitoff > totalfitpop:
    print("Success!")
