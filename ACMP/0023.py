number = int(input())
result = 0
for i in range (1, number+1):
    if number % i != 0:
        continue
    result += number / i
print(int(result))