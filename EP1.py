import matplotlib.pyplot as plt
import pandas as pd
import time
from tkinter.filedialog import askopenfilename
from tkinter import *

root = Tk()
filename = askopenfilename()
root.destroy()

data = pd.read_csv(filename, sep=',', index_col = 125)

start_time = time.time()

Locais = {}
for row in data.itertuples():
    CO_DOM = str(row[3]) + "-" + str(row[4])
    try:
        Locais[CO_DOM].append(row[44])
    except KeyError:
        Locais[CO_DOM] = [row[44]]

    CO_ESC = str(row[58]) + "-" + str(row[59])
    try:
        Locais[CO_ESC].append(row[44])
    except KeyError:
        Locais[CO_ESC] = [row[44]]

    CO_TR1 = str(row[63]) + "-" + str(row[64])
    try:
        Locais[CO_TR1].append(row[44])
    except KeyError:
        Locais[CO_TR1] = [row[44]]

    CO_TR2 = str(row[72]) + "-" + str(row[73])
    try:
        Locais[CO_TR2].append(row[44])
    except KeyError:
        Locais[CO_TR2] = [row[44]]

    CO_O = str(row[85]) + "-" + str(row[86])
    try:
        Locais[CO_O].append(row[44])
    except KeyError:
        Locais[CO_O] = [row[44]]

    CO_D = str(row[89]) + "-" + str(row[90])
    try:
        Locais[CO_D].append(row[44])
    except KeyError:
        Locais[CO_D] = [row[44]]

    CO_T1 = str(row[93]) + "-" + str(row[94])
    try:
        Locais[CO_T1].append(row[44])
    except KeyError:
        Locais[CO_T1] = [row[44]]

    CO_T2 = str(row[97]) + "-" + str(row[98])
    try:
        Locais[CO_T2].append(row[44])
    except KeyError:
        Locais[CO_T2] = [row[44]]

    CO_T3 = str(row[101]) + "-" + str(row[102])
    try:
        Locais[CO_T3].append(row[44])
    except KeyError:
        Locais[CO_T3] = [row[44]]


Locais_sem_dupl = {a:list(set(b)) for a, b in Locais.items()}

Lugares = {}
for lugar in Locais_sem_dupl:
    Lugares[lugar] = len(Locais_sem_dupl[lugar])

A = pd.DataFrame(list(Lugares.items()), columns=['Coordenadas', 'Quantidades'])

final = A.groupby('Quantidades').count()

final = final[final.index<85000]

final = final.reset_index()

x = final['Coordenadas']
y = final['Quantidades']
plt.plot(x, y)
#plt.ylim(0, 10)
print("--- %s seconds ---" % round(time.time() - start_time,2))
plt.show()

