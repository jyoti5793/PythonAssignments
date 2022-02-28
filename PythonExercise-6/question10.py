from datetime import datetime
def find_year(*d):
    given_date = datetime(*d)
    year = (lambda given_date :given_date.year)
    print(year(given_date))
find_year(2008, 6, 12, 10, 30, 0)