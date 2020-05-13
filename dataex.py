import pandas as pd
data = pd.read_csv('data.csv')
i=0
j=1
#while j < len(data):
#    j = data['openn'][i] - data['openn'][i+1]
#    i+=1
#    print(j)
k = 0

for i in range(3):
    print(data['openn'][i])
    j = data['openn'][i]
    if k<j:
        k = j
        print(k)
    
