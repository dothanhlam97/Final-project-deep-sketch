import plotly.plotly as py
import plotly.offline as py
import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt
import csv 


with open('circle.csv', 'rb') as csvfile:
    number = 0 
    sample = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in sample : 
        number = number + 1 
        print(number) 
        for x in row :
            data = [] 
            y = x.split(','); 
            for i in y : 
                data = np.append(data, float(i)) 
            plt.hist(data, 50)
            plt.title("Cirle")
            plt.xlabel("Value")
            plt.ylabel("Frequency")
            plt.show()
    


