# https://quera.org/problemset/235328

n, k = input().split()
n, k = int(n), int(k)

friends = input().split()

friends = [int(x)+1 for x in friends]

friends.sort()
# print(friends)

i = 0
result = 0
sum = 0
while i < len(friends):
    # print(friends[i])
    sum += friends[i]
    if sum > k:
        break
    elif sum == k:
        result += 1
        break
    else:
        result += 1
        i += 1

print(result)
