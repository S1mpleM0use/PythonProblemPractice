days = int(input())
flowers = 'GCV'

for i in range(1, days+1):
    flowers = flowers[2] + flowers[0] + flowers[1]

print(flowers)