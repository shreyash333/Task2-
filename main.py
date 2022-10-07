import GenData
import DBservice as db


# main function
starty = 2005       # start Year
endy = 2020         # end year
endm = 10           # end month
endd = 1            # end date

startfile = 20201001        # file name

for i in range(0, 5):

    # creating file and writing headers
    f = open('Lake_%d.txt' % (startfile+i), 'w')
    f.write('Appplication,date,Amount,load_date\n')
    f.close()

    # generating data
    GenData.genDataYear(starty-i, endy-1, 'Lake_%d.txt' %
                        (startfile+i))                          # year to year
    GenData.genDataMonth(1, endm-1, endy, 'Lake_%d.txt' %
                         (startfile+i))                         # month to month
    GenData.genDataDay(1, 1, endm, endy, 'Lake_%d.txt' %
                       (startfile+i))                           # day to day

# creating Database Lake_Data
db.createTable("Lake_data")

# copying data fom all files to DB (one record per day)
for i in range(0, 5):
    db.txtToSqlite("Lake_data", 'Lake_%d' % (startfile+i))

# printing all the data exist in DB and Stroing in a txt file
db.readAll("Lake_data")
