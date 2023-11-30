def is_leap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    """takes year and month and return number of days 
       in that year and that month"""
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year):
        month_days[1] = 29
    else:
        month_days[1] = 28
    return month_days[month-1]

year = int(input("enter a year: "))
month = int(input("enter a month: "))
days = days_in_month(year,month)
print(days)