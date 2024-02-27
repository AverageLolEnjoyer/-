import random

def gen_random(m, n, min_limit, max_limit):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(min_limit, max_limit))
        matrix.append(row)
    return matrix

n =                             int(input())
m =                             int(input())
min =                           int(input())
max =                           int(input())

print(gen_random(n, m, min, max))
