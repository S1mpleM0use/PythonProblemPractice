a1, a2, a3, b1, b2, b3 = map(int, input().split())

final = 0

rubles = [a1, a2, a3]
rubles.sort()

kgs = [b1, b2, b3]
kgs.sort()

for price, weight in zip(rubles, kgs):
    final += price * weight

print(final)