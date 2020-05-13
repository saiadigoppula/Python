import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('AzDev jul to dec inc records.xlsx')

print("Column headings:")
print(df[1][1])
