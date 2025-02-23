blocks = int(input())
counter = 0

while counter < blocks:
    counter += 1
    blocks -= counter

print(counter)