from hashlib import new
from matplotlib import pyplot as plt
import random
import numpy as np
N = 10
loops = 50
check = random.random()
print(check)


class solution:
    variable = [0] * N
    utility = 0


individual = solution()

for j in range(N):
    individual.variable[j] = random.randint(0, 100)
individual.utility = 0


def test_func(ind):
    utility = 0
    for i in range(N):
        utility = utility + ind.variable[i]
        return utility


newind = solution()
xaxis = np.array([-1])
yaxis = np.array([individual.utility])
for x in range(loops):
    print(individual.utility)

    for i in range(N):
        newind.variable[i] = individual.variable[i]
        change_point = random.randint(0, N - 1)
        newind.variable[change_point] = random.randint(0, 100)
        newind.utility = test_func(newind)
        xaxis = np.append(xaxis, [x])
        yaxis = np.append(yaxis, [individual.utility])
        if individual.utility <= newind.utility:
            individual.variable[change_point] = newind.variable[change_point]
            individual.utility = newind.utility

plt.plot(xaxis, yaxis)
plt.xlabel('Times Run')
plt.ylabel('Utility Score')

plt.show()
