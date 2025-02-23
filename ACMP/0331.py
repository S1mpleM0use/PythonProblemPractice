from datetime import datetime, timedelta


start = input()
hours_to_reach, minutes_to_reach = map(str, input().split())

time1 = datetime.strptime(start, "%H:%M")
time2 = timedelta(hours=int(hours_to_reach), minutes=int(minutes_to_reach))

result_time = time1 + time2

print(result_time.strftime("%H:%M"))