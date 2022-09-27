# itertools: product, permutations, combinations, accumulate, groupby and infinite interators
from itertools import product
from itertools import permutations
from itertools import accumulate
from itertools import groupby
from itertools import combinations, combinations_with_replacement
from itertools import count, cycle, repeat

# product
a = [1,2]
b = [3,4]
prod = product(a,b, repeat=2)
# print(list(prod))

# permutations
a = [1,2,3]
perm = permutations(a)
# print(list(perm))

# combinations
a = [1,2,3,4]
comb = combinations(a,2)
comb_wr = combinations_with_replacement(a,2)
# print(list(comb))
# print(list(comb_wr))

# accumulate
a = [1,2,5,4,3]
acc = accumulate(a, func=max)
# print(list(acc))

# groupby
# def smaller_than_3(x):
#     return x < 3

# a = [1,2,3,4]

# gp = groupby(a, key=smaller_than_3)
# for key, value in gp:
#     print(key, list(value))
    
# with lambda

a = [1,2,3,4]
gp = groupby(a, key=lambda x: x < 3)
# for key, value in gp:
#     print(key, list(value))

# infinite iterators

a = [1,2,3]
# for i in cycle(a):
#     print(i)
    
# for i in repeat(1,4):
#     print(i)
    



