scorelist = []
runs = 0
for x in range(5):
    print("CHECL?")
    runs += 100
    P = startingP
    for x in range(5):
        print(runs, P)
        score = scoreplotter(N, P, test_func, float(
            finalresults[0][0]), float(finalresults[0][1]), runs)
        scorelist.append([runs, P, score[3], score[4]])
        P += 50
scorelist = tabulate(scorelist, headers=[
    "Runs", "Pop Size", "Best", "Average"], tablefmt="pretty")
print(scorelist)
f.write(scorelist)