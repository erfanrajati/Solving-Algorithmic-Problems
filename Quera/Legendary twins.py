# https://quera.org/problemset/197002

inputCount = int(input())

def isShifted(str1, str2):
    if str1 == str2:
        return True
    else:
        shiftedStr = str2
        for _ in range(len(str1)):
            shiftedStr = shiftedStr[-1] + shiftedStr[:-1]
            if shiftedStr == str1: 
                return True
        return False


inputList = []
for _ in range(inputCount):
    n1, n2 = input().split()
    inputList.append((n1, n2))


for n1, n2 in inputList:
    if isShifted(n1, n2) or isShifted(n1, n2[::-1]):
        print('YES')
    else:
        print('NO')