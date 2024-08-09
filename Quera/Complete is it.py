# https://quera.org/problemset/282

userIn = int(input())
divisors = []
for i in range(1, userIn):
    if userIn % i == 0:
        divisors.append(i)

print('YES' if userIn == sum(divisors) else 'NO')