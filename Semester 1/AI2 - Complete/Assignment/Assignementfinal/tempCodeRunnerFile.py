        worsebaby = mutatedgenes[0]
#         bestbaby = mutatedgenes[0]
# # Loop through mutated genes until both the best and worst individuals have been found
#         for x in mutatedgenes:
#             if x.fitness < bestbaby.fitness:
#                 bestbaby = x
#             if x.fitness > worsebaby.fitness:
#                 worsebaby = x
#         # Get the index number of the worst individual in the array.
#         indexno = mutatedgenes.index(worsebaby)
#         # Replace the worst individual in the population
#         mutatedgenes[indexno] = bestbaby
#         # Make population a copy of the newly cre