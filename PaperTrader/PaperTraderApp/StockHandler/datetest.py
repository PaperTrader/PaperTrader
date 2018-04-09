import datetime
def test():
    weekdays = [0, 1, 2, 3, 4]
    #today = datetime.datetime.today()
    today = datetime.datetime(2018, 3, 30, 00, 00, 00)
    print(today)
    if(today.weekday() in weekdays):
        return str(today).split()[0]
    shift = datetime.timedelta(max(1, (today.weekday() + 6) % 7 - 3))
    today = today - shift
    return str(today).split()[0]
print(test())

