        change_point = random.randint(0, N - 1)
        newind.variable[change_point] = random.randint(0, 100)
        newind.utility = test_func(newind)
        xaxis = np.append(xaxis, [x])
        yaxis = np.append(yaxis, [individual.utility])
        if individual.utility <= newind.utility:
            individual.variable[change_point] = newind.variable[change_point]
            individual.utility = newind.utility