n = int(input())

result = 0
for i in range(3, n+1):
    queens_per_side = i - 2
    total_queens = queens_per_side * 2
    result += total_queens

print(result)
