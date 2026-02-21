from collections import defaultdict

# https://www.geeksforgeeks.org/python/defaultdict-in-python/

d = defaultdict(list)

d['fruits'].append('apple')
d['fruits'].append('banana')
d['fruits'].append('melons')

d['vegetables'].append('carrot')
d['vegetables'].append('peas')
d['vegetables'].append('tomato')

print(d)

print("_______________________")

print(" fruits : " + str(d['fruits']) )

print( "vegetables: " + str(d['vegetables']) )