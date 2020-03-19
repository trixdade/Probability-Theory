from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
   
    
# печать таблицы
def printTable(data, thead):
    table1 = PrettyTable(thead)
    tdata = data[:]
    columns = len(thead)
    while tdata:
        table1.add_row(tdata[:columns])
        tdata = tdata[columns:]
    print(table1)


# построение графиков
def printGraphics(x, y1, y2):
    plt.figure(1)
    plt.title("F and F_exp graph")     
    for i in range(len(x) - 1):
        myx_value = np.linspace(x[i], x[i+1], 50)
        myy_value = np.ones(50) * y2[i]
        plt.plot(myx_value, myy_value, color="red", label = "F_exp(x)")
    
    plt.plot(x, y1, color="black", label="F(x)")
