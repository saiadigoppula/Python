import pandas as pd

df = pd.read_csv("TATAMOTORS.csv")
print(len(df))

count = 0
x = 2
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven =0
eight = 0
nine = 0
ten = 0
other = 0
value = 0
while (x)<len(df):
    #print("x",x)
    cnt = 0
    if((df['openn'][x] > df['close'][x])):
        y = x-1
        #print("y1",y)
        while (y+10)<len(df):
            y = y +1
            if((df['openn'][y] > df['close'][y])):
                value +=1
                cnt = cnt +1
                #print("y2",y)
            else:
                if(1==cnt):
                    count = cnt
                    #print(x,y)
                    #print("from",df['date'][x],"to",df['date'][y-1],"count = ",count)
                    #print(df['close'][x])
                    x = y-1
                    one += 1
                    #print("x2",x)
                    cnt = 0
                    break
                elif(2==cnt):
                    two +=1
                    x = y-1
                    cnt = 0
                    break

                elif(3==cnt):
                    three+=1
                    #print("3",three)
                    x = y-1
                    cnt = 0
                    break

                elif(4==cnt):
                    four+=1
                    x = y-1
                    cnt = 0
                    break

                elif(5==cnt):
                    five +=1
                    x = y-1
                    cnt = 0
                    break

                elif(6==cnt):
                    six +=1
                    x = y-1
                    cnt = 0
                    break

                elif(7==cnt):
                    seven +=1
                    x = y-1
                    cnt = 0
                    break
                elif(8==cnt):
                    eight +=1
                    x = y-1
                    cnt = 0
                    break
                elif(9==cnt):
                    nine +=1
                    x = y-1
                    cnt = 0
                    break
                elif(10==cnt):
                    ten +=1
                    x = y-1
                    cnt = 0
                    break
                    
                else:
                    other +=1
                    cnt = 0
                    break
                    x = y-1
                    break
                    #print("x3",x)
    x = x+1

print("value",value)
print("1",one   ,(one/value)*100)
print("2",two   ,(two/value)*100)
print("3",three  ,(three/value)*100)
print("4",four   ,(four/value)*100)
print("5",five   ,(five/value)*100)
print("6",six    ,(six/value)*100)
print("7",seven    ,(seven/value)*100)
print("8",eight    ,(eight/value)*100)
print("nine",nine   ,(nine/value)*100)
print("ten",ten    ,(ten/value)*100)
print("other",other   ,(other/value)*100)
                
