# https://quera.org/problemset/234249

stones = input().split(' ')
hit = input()

i = stones.index(hit)

i = 1 if i == 0 else i

print(7 - i)

