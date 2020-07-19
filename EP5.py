import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random
import numpy as np
from tkinter.filedialog import askopenfilename
from tkinter import *
from collections import defaultdict

root = Tk()
filename = askopenfilename()
root.destroy()

file1 = open(filename, 'r')
Lines = file1.readlines()

count = 0
arestas = []
for line in Lines:
    if count == 0:
        linha1 = line
    elif count == 1:
        linha2 = line
    else:
        arestas.append(line.split())
    count += 1


class Graph(object):

    def __init__(self, arestas):
        self.adj = defaultdict(set)
        self.add_arestas(arestas)

    def get_arestas(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def add_arestas(self, arestas):
        for u, v in arestas:
            self.adj[u].add(v)
            self.adj[v].add(u)

    def get_graus(self):
        dict_graus = {}
        for each in self.adj:
            dict_graus[each] = len(self.adj[each])
        return dict_graus

    def get_vertices(self):
        return list(self.adj.keys())

    def get_adjacencias(self, v):
        return self.adj[v]


grafo_grande = Graph(arestas)

#Contagio e recuperacao:
c = 0.7
r = 0.1

#Pega Vertices do grafo e define um dicionario com S em todos
vertices = grafo_grande.get_vertices()
pessoas = dict.fromkeys(vertices, 'S')

estados = list(pessoas.values())
I = estados.count('I')
R = estados.count('R')
S = estados.count('S')
tbl_estados = pd.DataFrame(columns=("I", "R", "S"))
inicial = {"I": I,"R": R,"S": S}
tbl_estados = tbl_estados.append(inicial, ignore_index=True)
#tbl_estados = tbl_estados.append({"CICLO": 5151,"I": 456456,"R": 456456,"S": 86867}, ignore_index=True)
ciclo = 1

SORTUDO = random.choice(vertices)
pessoas[SORTUDO] = 'I'
estados = list(pessoas.values())
I = estados.count('I')
R = estados.count('R')
S = estados.count('S')
tbl_estados = tbl_estados.append({"I": I,"R": R,"S": S}, ignore_index=True)


while list(pessoas.values()).count('I')>0:
    for each in pessoas:
        if pessoas[each] == 'I':
            x = random.randrange(100)/100
            if x <= r:
                pessoas[each] = 'R'
            else:
                adjacencias = grafo_grande.get_adjacencias(each)
                for cada in adjacencias:
                    if pessoas[cada] == 'S':
                        y = random.randrange(100)/100
                        if y <= c:
                            pessoas[cada] = 'I'
    estados = list(pessoas.values())
    I = estados.count('I')
    R = estados.count('R')
    S = estados.count('S')
    tbl_estados = tbl_estados.append({"I": I,"R": R,"S": S}, ignore_index=True)
    ciclo += 1

sns.set()
Tempo = list(tbl_estados.index)
I = list(tbl_estados.I)
R = list(tbl_estados.R)
S = list(tbl_estados.S)

fig, ax = plt.subplots()

ax.bar(Tempo, R, label = 'Recuperados', bottom = np.array(S)+np.array(I))
ax.bar(Tempo, I, label = 'Infectados', bottom=S)
ax.bar(Tempo, S, label = 'Suscetíveis')

ax.set_ylabel('Quantidade')
ax.set_xlabel('Tempo')
ax.legend()

plt.show()

plt.plot(tbl_estados)