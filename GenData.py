
from datetime import date
import GeneralService as gs
import random


# function to generate year to year data
def genDataYear(y1, y2, fn):
    # constant values application and load date
    ld = str(date.today())
    App = "Lake"
    try:
        fk = open(fn, 'a')
        # generating and storing the data in given file
        for i in range(y1, y2+1):                       # Year loop
            for j in range(1, 13):                      # month loop
                for k in range(1, gs.getdays(j, i)+1):  # day loop
                    for h in range(0, 24):              # hour loop
                        # generating date time
                        dt = ('%d-%s-%s %s:00:00' %
                              (i, str(j).zfill(2), str(k).zfill(2), str(h).zfill(2)))
                        # generating random value
                        am = round(random.uniform(1.0000000000, 10.0000000000), 10)
                        # writing the data to txt file
                        datastr = ('%s,%s,%f,%s' % (App, dt, am, ld))
                        fk.write(datastr+'\n')
    except:
        print("Unable to generate year to year data")


# function to generate month to month of same year data
def genDataMonth(m1, m2, y, fn):
    # constant values application and load date
    ld = str(date.today())
    App = "Lake"
    try:
        fk = open(fn, 'a')
        # generating and storing the data in given file
        for j in range(m1, m2+1):                   # month loop
            for k in range(1, gs.getdays(j, y)+1):  # day loop
                for h in range(0, 24):              # hour loop
                    # generating date time
                    dt = ('%d-%s-%s %s:00:00' %
                          (y, str(j).zfill(2), str(k).zfill(2), str(h).zfill(2)))
                    # generating random value
                    am = round(random.uniform(1.0000000000, 10.0000000000), 10)
                    # writing the data to txt file
                    datastr = ('%s,%s,%f,%s' % (App, dt, am, ld))
                    fk.write(datastr+'\n')
    except:
        print("Unable to generate month to month data")


# function to generate day to day of saem month and year data
def genDataDay(d1, d2, m, y, fn):
    # constant values application and load date
    ld = str(date.today())
    App = "Lake"
    try:
        fk = open(fn, 'a')
        # generating and storing the data in given file
        for k in range(d1, d2+1):           # day loop
            for h in range(0, 24):          # hour loop
                # generating date time
                dt = ('%d-%s-%s %s:00:00' %
                      (y, str(m).zfill(2), str(k).zfill(2), str(h).zfill(2)))
                # generating random value
                am = round(random.uniform(1.0000000000, 10.0000000000), 10)
                # writing the data to txt file
                datastr = ('%s,%s,%f,%s' % (App, dt, am, ld))
                fk.write(datastr+'\n')
    except:
        print("Unable to generate day to day data")
