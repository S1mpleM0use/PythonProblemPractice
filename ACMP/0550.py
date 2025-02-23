year = int(input())
if year < 10:
    new_year = ''.join('000' + str(year))

elif year < 100:
    new_year = ''.join('00' + str(year))

elif year < 1000:
    new_year = ''.join('0' + str(year))

else:
    new_year = year

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f'12/09/{new_year}')
else:
    print(f'13/09/{new_year}')