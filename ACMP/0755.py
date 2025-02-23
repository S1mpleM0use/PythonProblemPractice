x, y, z = map(int, input().split())

if (x+y) - z < 0:
    print('Impossible')
else:
    print((x+y) - z)
