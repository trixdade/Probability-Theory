import math as m
from collections import Counter
from LR_functions import *
from table_graphics import *


# Program starts
p = float(input("Enter probability value: "))
n = int(input("Enter number of experiments: "))

# проведение экспериментов n раз с вероятностью p
# в массив numbers записываются значения случайной величины
numbers = []
experiment(numbers, n, p)

Data = [] # здесь будут все данные для таблицы
c = Counter(numbers) # считаем количество каждого элемента в numbers
maximum = max(c) # максимальная случайная величина
for x in range(1, maximum + 1):
    d = dict(c)
    Data.append(x) # сначала добавляем значение СВ
    Data.append(d.get(x, 0)) # количество выпадений СВ X, если нет, то 0
    Data.append(round(d.get(x, 0)/n, 3)) # частота СВ 

    
thead = ["Value", "Amount", "Freq"] # задаем заголовки столбцов
printTable(Data, thead) # печатаем таблицу 1

Data.clear() # потом будем класть сюда данные из след таблицы

# подготовка структур данных для таблицы
E = []
E_exp = []
E_diff = []
E_lib = []
D = []
D_exp = []
D_diff = []
Me_exp = []
R_exp = []
table = PrettyTable()


# создаем названия колонок
table.add_column("E",[E])
table.add_column("E_exp", [E_exp])
table.add_column("E_diff", [E_diff])
table.add_column("E_lib", [E_lib])
table.add_column("D", [D])
table.add_column("D_exp", [D_exp])
table.add_column("D_diff", [D_diff])
table.add_column("Me_exp", [Me_exp])
table.add_column("R_exp", [R_exp])

E.append(round(1/p,3)) # теоретическое мат ожидание
M_exp = np.mean(numbers)
E_exp.append(round(M_exp, 3)) # выборочное среднее
E_diff.append(round(m.fabs(1/p - M_exp), 5)) # разница
E_lib.append(round(np.mean(np.random.geometric(p, n)), 5)) # мат ожидание из библиотеки
D.append(round((1-p)/(p*p), 3)) # дисперсия


# подсчет выборочной дисперсии 
s = 0
M = np.mean(numbers) # выборочное среднее для вычисления выборочной дисперсии
for xi in numbers:
    s = s + (xi - M)*(xi - M)

D_exp.append(round(s/n,5)) # выборочная дисперсия 
D_diff.append(round(np.fabs(D_exp[0] - D[0]),5)) # разница
Me_exp.append(findMediana(numbers)) # медиана

R_exp.append(max(numbers)-min(numbers)) # разность макс и мин значений в выборке

print(table)  # Печатаем таблицу 2

        
y2 = [] # понадобится для построения графика F_exp

# в Data будет вся информация для третьей таблицы
difference = [] # понадобится для подсчета максимальной разницы в выборке    
maximum = max(c)
P_th = 0
Frequency = 0
for x in range(1, maximum + 1):
    d = dict(c)
    
    Data.append(x) # value
    
    P_th = (1-p)**(x-1) * p # probability
    Data.append(round((1-p)**(x-1) * p, 5)) 
    
    Frequency = d.get(x, 0)/n # frequency
    Data.append(round(Frequency, 5))
    
    diff = ((1-p)**(x-1) * p) - d.get(x, 0)/n # diff
    difference.append(m.fabs(diff))
    Data.append(m.fabs(round(diff,5)))
    y2.append(d.get(x, 0)/n)
        
max_diff = max(difference)    

thead = ["Value", "Probability", "Freq", "Diff"]
printTable(Data, thead) # печатаем таблицу 3

print('Max difference = ', round(max_diff,5))




y1 = [] # понадобится для построения графика F
summ = 0
x = range(1, maximum + 1)
for value in range(0, len(y2)):
    summ += (1-p)**value * p
    y1.append(summ)
        
# получаем значения интегральной функции F_exp
for i in range(1, len(y2)): 
    y2[i] = y2[i] + y2[i-1] 

D = [] # мера расхождения графиков
for i in range(1,len(y2)):
    D.append(m.fabs(y1[i] - y2[i]))
    
D_max = max(D)
print("Максимальное расхождение графиков = ", D_max)

printGraphics(x, y1, y2)