

Assignment :

1. Create 5 flat files with .txt extension which will contain data, where it will have four columns Application, date, Amount and load_date. Load date and application will be constant for all entries and date and amount will change.

2.As mentioned in point.1, 5 files needs to be generated which will have below req data. 

Lake_20201005.txt - Data from1 Jan 2001 till 1 OCT 2020 for every hour an random amount.
Lake_20201004.txt - Data from1 Jan 2002 till 1 OCT 2020 for every hour an random amount. 
Lake_20201003.txt - Data from1 Jan 2003 till 1 OCT 2020 for every hour an random amount. 
Lake_20201002.txt - Data from1 Jan 2004 till 1 OCT 2020 for every hour an random amount. 
Lake 20201001.txt = Data from1 Jan 2005 till 1 OCT 2020 for every hour an random amount.

Example record :

Lake_20201005.txt 
Application, date, amount, load_date 
Lake, 2001-01-01 00:00:00, 3.2312323123,2020 10-05
Lake, 2001-01-01 01:00:00, 4.4324234432,2020 10-05

3. Create a table in sqlite (Python inbuilt DB) with same structure of file and store only one record for each Date programmatically by comparing two files.
Means, Lake_20201001.txt will be loaded for all dates, but from Lake_20201002.txt only records of 2004 to 2005 should be loaded.
Same should be for other 3 files.

While working on this assignment, pls try to :
1. Make the solution above as a package by using your thought process.
2. Functional programming.
3. Database handlers saparated from application handlers.
4. Exceptional handling wherever you think is necessary.