def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


n = int(input())

if n == 1:
    print(0)
elif is_even(n):
    print(n // 2)
else:
    print(n)
