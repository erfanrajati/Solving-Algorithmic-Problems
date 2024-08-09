# https://quera.org/problemset/220669

userIn = int(input())

string = '.' * (userIn-1) + 'D' + '.' * (userIn-1)
string = list(string)

for i in range(userIn-1, 0, -1):
    print(''.join(c for c in string))
    string[i] = '.'
    string[len(string)-1-i] = '.'
    j = i-1
    string[j] = 'D'
    string[len(string)-1-j] = 'D'

last_row = ['.' if i%2 else 'D' for i in range(len(string))]
print(''.join(c for c in last_row))