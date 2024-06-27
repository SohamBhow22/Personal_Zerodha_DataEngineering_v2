##Area to import required packages
from pathlib import Path
import sqlalchemy as sql
import pyodbc
import glob
import pandas as pd


##Area to define all required functions
def get_file_date(file):
    filename = Path(file).stem
    ##print(type(filename))
    filefulldate = filename[9:]
    fileyear = filename[9:13]
    filemonth = filename[13:15]
    filedate = filename[15:17]
    print(filefulldate)
    ##print(fileyear)
    ##print(filemonth)
    ##print(filedate)

def read_daily_file(filename):
    get_file_date(filename)
    dailyDF = pd.read_csv(filename)
    print(dailyDF)
    ##print(list(dailyDF.columns))
    countofstocks = len(dailyDF.index)
    print("No. of Stocks each day:", countofstocks)
    for i in range(0, 2, 1): #2 is to be replaced by countofstocks
        iterate_dataframe(dailyDF, i)
    #insert_into_datawarehouse(dailyDF)

def iterate_dataframe(df, index):
    ##countOfStocks = len(df.index)
    colnames = list(df.columns)
    noofcolumns = len(colnames)
    ##print(colnames) #Works
    ##print(noofcolumns) #Works
    for i in range(0, noofcolumns):
        print(df[colnames[i]].iloc[index])

'''
def insert_into_datawarehouse(datadf):
    engine = sql.create_engine('mssql+pyodbc://@SOHAM-DELLG15\SQLEXPRESS/TESTDB?trusted_connection=yes&driver=ODBC+Driver+18+for+SQL+Server')
    print(datadf)
    d = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Number': [2056, 2154635, 19456546, 184545]}
    DF = pd.DataFrame(d)
    print(DF)
    ##datadf.to_sql('TEST_CONN', DF)
    with engine.connect() as conn :
        result = conn.execute("Select * from dbo.STOCKMETADATA")
    print(DF)
      
    # print the result
    ##for row in result:
    ##    print(row.STOCKNAME)
'''

##Main Area
files = glob.glob('D:/Soham/Projects/0. Datasets/Zerodha Data/Daily/Holdings_20230711.csv')
countOfFiles = 0
for file in files:
    countOfFiles=countOfFiles+1
    print(file)
    ##dailyDF = pd.read_csv(file)
    ##getFileDate(file)
    read_daily_file(file)
    ##print(len(Path(file).stem))
print(countOfFiles)    