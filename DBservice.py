from logging import exception
import sqlite3

# connecting to the sqlite DB
connection_obj = sqlite3.connect('Lake.db')
cursor_obj = connection_obj.cursor()


# function to create a table wiith 4 columns Application, date, Amount and load_date
def createTable(tabname):
    try:
        cursor_obj.execute('DROP TABLE IF EXISTS %s' % (tabname))
        table = 'CREATE TABLE %s ( Appplication VARCHAR(255) NOT NULL, date CHAR(25) NOT NULL, Amount FLOAT NOT NULL, load_date CHAR(25) NOT NULL );' % (
            tabname)
        cursor_obj.execute(table)
    except:
        print("Unable to create %s table." % (tabname))


# fucntion to copy data from text to sqlite and checking whether the data for that day already exist or not
def txtToSqlite(tabname, filename):
    # reading data from the source file
    try:
        f = open('%s.txt' % (filename), 'r')
    except:
        print("Unable to read %s file." % (filename))
    # making list of existind date data
    existlist = []
    try:
        statement = 'SELECT * FROM %s' % (tabname)
        cursor_obj.execute(statement)
        output = cursor_obj.fetchall()
    except:
        print("Unable to read data from %s table." % (tabname))
    for row in output:
        if row[1][0:10] not in existlist:
            existlist.append(row[1][0:10])
        else:
            continue

    # iterating throught all the values
    isheader = True
    for l in f:
        l = l.replace('\n', '')
        if isheader == True:
            isheader = False
            continue
        # conveting string to list of values and checking its existance
        ls = l.split(",")
        if ls[1][0:10] not in existlist:
            # inserting data into sqlite DB
            existlist.append(ls[1][0:10])
            ls = str(tuple(ls))
            try:
                query = ('INSERT INTO %s VALUES %s;' % (tabname, ls))
                cursor_obj.execute(query)
            except:
                print("Unable to write data in %s table." % (tabname))
        else:
            # iterating to next element in the list
            continue


# function to read all values
def readAll(tabname):
    # reading data from sqlite DB
    try:
        query = 'SELECT * FROM %s' % (tabname)
    except:
        print("Unable to read data from %s table." % (tabname))
    cursor_obj.execute(query)
    print("All Data of Lake_data DB")
    output = cursor_obj.fetchall()
    # creating output file
    fo = open('sqlite_DB.txt', 'w')
    # printing and storing the data
    for row in output:
        # print(row)
        fo.write(str(row)+'\n')
