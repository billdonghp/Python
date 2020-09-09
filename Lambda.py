from functools import reduce

ls = [1,2,3,4,5,6]

print(list(filter(lambda x : x % 2 == 0,ls)))

print(list(map(lambda x :x * x , ls)))

print(reduce(lambda a,b : a + b, ls))

