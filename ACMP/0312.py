first, second, the_number = map(int, input().split())

d = second - first
counter = 2
progression = [first, second]

for i in range(the_number):
    progression.append(first + (counter*d))
    counter += 1

print(progression[the_number-1])
