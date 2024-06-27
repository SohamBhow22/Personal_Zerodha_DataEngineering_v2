print("hello1")
import glob
import pandas as pd
files = glob.glob('D:/Soham/Projects/0. Datasets/Zerodha Data/Daily/*.csv')
for file in files:
    print(file)