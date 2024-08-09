# https://quera.org/problemset/218361

row1 = tuple(int(i) for i in input().split(' '))
row2 = tuple(int(i) for i in input().split(' '))
print(list(zip(row1, row2)).count((1, 1)))