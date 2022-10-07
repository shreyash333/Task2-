

# function to get number of days in a month
def getdays(m, y):
    # feb month with leap year
    if((m == 2) and ((y % 4 == 0) or ((y % 100 == 0) and (y % 400 == 0)))):
        return 29

    # normal feb month
    elif(m == 2):
        return 28

    # month having 31 days (jan, mar, may, jul, aug, oct, dec)
    elif(m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        return 31

    # month having 30 days (april, june, sep, nov)
    else:
        return 30
