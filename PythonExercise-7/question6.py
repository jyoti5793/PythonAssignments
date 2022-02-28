#given_date = datetime(2010, 6, 12)

from datetime import datetime
from datetime import date
def find_day(*day):
    try:
        given_date = datetime(*day)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        x = date.weekday(given_date)
        print(days[x])
    except:
        print('Oops! An error occurred.')
find_day(2010, 6, 12)