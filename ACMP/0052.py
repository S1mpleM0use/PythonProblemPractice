ticket_number = input()
if int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2]) == int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5]):
    print('YES')
else:
    print('NO')