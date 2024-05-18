inputs = [] # to have inputs organized

# getting inputs, cleaning the ' ' characters and filling the list.
while 1:
    temp = input().replace(' ', '')
    if temp == '0'*16:
        break
    inputs.append(temp)
    
# turning in string format card numbers into lists 
# so we can use indexing for further calculations
for card in inputs:
    temp = [char for char in card]
    inputs[inputs.index(card)] = temp
    
print(inputs)

def isValid(card: list):
    '''Follows the procedure provided in question. But simplified'''
    odds_doubled = [(int(num)*2) % 9 for num in card[::2]]
    evens = [int(num) for num in card[1::2]]
    result = sum(odds_doubled) + sum(evens)
    return not bool(result % 10)

# Finally we test
for card in inputs:
    if isValid(card):
        print('Yes')
    else:
        print('No')


'''
inputs test
6104 3376 7866 1545
6104 3376 7866 1546
5022 2910 0140 7954
0000 0000 0000 0000
'''