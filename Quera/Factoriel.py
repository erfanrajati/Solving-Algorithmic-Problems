# https://quera.org/problemset/589

userIn = int(input())

result = 1
for i in range(1, userIn + 1):
    result *= i

print(result)