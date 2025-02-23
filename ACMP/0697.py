from math import ceil
l, w, h = map(int, input().split())
wall1 = l * h
wall2 = w * h
answer = ceil(((wall1 * 2 + wall2 * 2) / 16))
print(answer)

