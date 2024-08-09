# https://quera.org/problemset/235327

inputs = int(input())
tests = []

for _ in range(inputs):
    a, b, h = input().split(' ')
    a, b, h = int(a), int(b), int(h)
    tests.append((a, b, h))

for test in tests:
    a, b, h = test
    currentHeight = 0
    days = 0

    while True:
        days += 1
        currentHeight += a
        if currentHeight >= h: break
        currentHeight -= b

    print(days)