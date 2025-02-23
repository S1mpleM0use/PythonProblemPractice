from math import ceil
k, n = map(int, input().split())

pages = ceil(n/k)

string_number = n % k

if string_number == 0:
    print(pages, n // pages)
else:
    print(pages, string_number)
