from datetime import date,timedelta
today = date.today()
yesterday = today-timedelta(1)
tomorrow = today+timedelta(1)
print(today)
print(yesterday)
print(tomorrow)