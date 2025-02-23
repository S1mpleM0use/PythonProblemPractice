number = int(input())
mass = list(map(int, input().split()))

mass.sort()

print(mass[0], mass[number-1])
