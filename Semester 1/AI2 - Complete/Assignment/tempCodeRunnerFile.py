def fitness_scatter_plotter(ind, N):
    fitness = 0
    fitnesstotal = 0
    fitnessarray = []
    first = (ind.gene[0] - 1)**2
    for i in range(1, N):
        fitness += i * (((2 * ind.gene[i]**2) - (ind.gene[i - 1]))**2)
        fitness = fitness + first
        fitnessarray.append(fitness)
        fitnesstotal += fitness
    return fitnessarray, fitnesstotal