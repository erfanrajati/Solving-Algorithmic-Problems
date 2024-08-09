# https://quera.org/problemset/220668

n, m = input().split(' ')
n, m = int(n), int(m)

requests = []

for i in range(m):
    s, l = input().split(' ')
    s, l = int(s) - 1, int(l)
    requests.append((s, l))

initialState = '0' * n

for s, l in requests:
    start = initialState.find('0' * l, s)
    if start != -1:
        initialState = list(initialState)
        initialState[start : start+l] = '1' * l
        initialState = ''.join(initialState)
    print(initialState)
