import requests
import json
import csv
import os

lists = ['TATAMOTORS'] 
        
 

   

length = len(lists) 
   
for i in range(length):
    x = lists[i]+".NS"
    url = 'https://api.worldtradingdata.com/api/v1/history'
    params = {
      'symbol': x,
      'api_token': 'EfopvFRc7g1bEnX6vpfifY0spt1rHFWDy1m4yjAHI6iSrMGBJJOS6z8Q9Tg8'
    }
    response = requests.request('GET', url, params=params)
    response.json()
    sai = response.json()
    rai = sai['history']
    with open("demo.csv","w",newline='') as f:
        thewriter = csv.writer(f)
        #thewriter.writerow(['date','openn','close','high','low','volume'])
        for p_id, p_info in rai.items():
            #print(p_id,end = ',')
            for key in p_info:
                if(key == "open"):
                    openn =  float(p_info[key])
                    #print(openn,end = ',')

                if(key == "close"):
                    close =  float(p_info[key])
                    #print(close,end = ',')

                if(key == "high"):
                    high =  float(p_info[key])
                    #print(high,end = ',')

                if(key == "low"):
                    low =  float(p_info[key])
                    #print(low,end = ',')

                if(key == "volume"):
                    volume =  float(p_info[key])
                    #print(volume)
            thewriter.writerow([p_id,openn,close,high,low,volume])
            
    with open('demo.csv', 'r') as textfile:
        with open(lists[i]+".csv","w",newline='') as ff:
            thewriterr = csv.writer(ff)
            thewriterr.writerow(['date','openn','close','high','low','volume'])
            for row in reversed(list(csv.reader(textfile))):
                date = row[0]
                #print(date)
                openn = row[1]
                close = row[2]
                high = row[3]
                low = row[4]
                volume = row[5]
                thewriterr.writerow([date,openn,close,high,low,volume])
                    #print(', '.join(row))
                    #print(row[1])
    os.remove("demo.csv")
    print("fineshed"+lists[i])
print("FINISHED ALL!")
