# https://quera.org/problemset/209103

h, w = input().split()
h, w = int(h), int(w)

for i in range(h * 2 + 1):
    if i % 2:
        for j in range(w + 1):
            print('| ', end='')
        print()
    else:
        for j in range(w):
            print(' _', end='')
        print()

