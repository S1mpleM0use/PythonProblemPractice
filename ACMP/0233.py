bridges = int(input())
height = list(map(int, input().split()))
check = 0

for i in range(len(height)):
    if height[i] - 437 <= 0:
        print(f'Crash {i+1}')
        check = 1
        break
if check == 0:
    print('No crash')