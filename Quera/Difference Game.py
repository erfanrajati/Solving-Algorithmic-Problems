# https://quera.org/problemset/87176

def game(userIn: int):
    temp = str(userIn)
    result = abs(int(temp[1]) - int(temp[0]))
    return result