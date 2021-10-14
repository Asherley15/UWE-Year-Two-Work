from hashlib import new
from matplotlib import pyplot as plt
import random
import numpy as np

N = 10
P = 50
(((((({{{{}}}}))))))


class individual:
    def __init__(self) -> None:
        pass
    gene = []
    fitness = 0


population = []

for x in range(0, P):
    tempgene = []
    for y in range(0, N):
        tempgene.append(random.randint(0, 1))
    newind = individual()
    newind.gene = tempgene.copy()
    population.append(newind)


def test_func(pop):
    fitness = 0
    for x in pop:
        for y in x.gene:
            if y == 1:
                fitness += 1

    print('Total fitness:', fitness)
    return fitness


offspring = []


def breed_pop(population):
    global offspring
    offspring.clear()
    for i in range(0, P):
        parent1 = random.randint(0, P - 1)
        off1 = population[parent1]
        parent2 = random.randint(0, P - 1)
        off2 = population[parent2]

        if off1.fitness > off2.fitness:
            offspring.append(off1)

        else:
            offspring.append(off2)
    return offspring


breed_pop(population)
if test_func(offspring) > test_func(population):
    print('Breed successful')
    population = offspring
else:
    breed_pop(population)
    print('Breed failed')
