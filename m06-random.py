import random

nbrs = [1,2,3,4,5,6,7,8,9,10]
print('i\trand')
print('==\t====')
for i in range(10):
    print(f'{i}\t{random.choice(nbrs)}')