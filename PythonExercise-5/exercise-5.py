#question1
from datetime import datetime
from datetime import date
today = datetime.now()
print(today)

#question2
dob_time = datetime(1995, 6, 14, 10, 37, 50, 0)
print("Month",dob_time.month)
print("Minutes", dob_time.minute)

#question3
given_date = datetime(2011, 10, 12)
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
x = date.weekday(given_date)
print(days[x])

#question5