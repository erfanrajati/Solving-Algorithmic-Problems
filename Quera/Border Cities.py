# https://quera.org/problemset/228669

cityHeight = int(input())
cityWidth = int(input())
if cityWidth == 1 or cityHeight == 1:
    print(cityWidth * cityHeight)
else:
    print(cityHeight * 2 + cityWidth * 2 - 4)