from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import style

style.use('fivethirtyeight')

df = pd.read_csv("BPCLtwomin.csv")


'''xs = [1,2,3,4,5,6]
ys = [5,4,6,5,6,7]'''

xs = np.array(df['openn'],dtype = np.float64)



ys =  np.array(df['close'],dtype = np.float64)

def best_fit_slop_and_intercept(xs,ys):
    m = (  ((mean(xs) * mean(ys)) - mean(xs*ys)) /
           ((mean(xs)*mean(xs)) - mean(xs*xs)))

    b = mean(ys) - m*mean(xs)
    
    

    return m , b



def squared_error(ys_orig,ys_line):
    return sum((ys_line-ys_orig)**2)



def coef_of_deter(ys_orig,ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_reg = squared_error(ys_orig,ys_line)
    squared_error_y_mean = squared_error(ys_orig,y_mean_line)
    return 1 - (squared_error_reg/squared_error_y_mean)



m,b = best_fit_slop_and_intercept(xs,ys)

reg_lin = [(m*x)+b for x in xs]


#plt.Scatter(xs,reg_lin)
#plt.show()

pre_x = 499.4
pre_y = (m*pre_x)+b

r_sqr = coef_of_deter(ys,reg_lin)

print(r_sqr)


print(pre_y)

#print(m,b)
'''
plt.scatter(xs,ys)
plt.scatter(pre_x,pre_y,color='r')
plt.plot(xs,reg_lin,color='g')

plt.show() '''
