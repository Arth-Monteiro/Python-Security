from itertools import permutations

res = permutations("ABC", 3)

for i in res:
    print("".join(i))
