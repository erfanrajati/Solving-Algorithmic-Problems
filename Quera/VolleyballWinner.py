# https://quera.org/problemset/232025

games_played = int(input())

games_data = []
for _ in range(games_played):
    points = input()
    sequence = input()
    games_data.append(sequence)

games_analyzed = [
    (game, True) if game.count('Q') > game.count('C') else 
    (game, False) 
    for game in games_data
]


for game, result in games_analyzed:
    print('Quera' if result else 'CodeCup')