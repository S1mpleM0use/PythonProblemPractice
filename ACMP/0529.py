from math import sqrt

x1, y1, x2, y2 = map(int, input().split())

print('{0:.5f}'.format((sqrt((x2-x1)**2 + (y2 - y1)**2))))