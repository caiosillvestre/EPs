import matplotlib.pyplot as plt
import pandas as pd
import time
import seaborn as sns
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

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


grafo_grande = Graph(arestas)

graus = grafo_grande.get_graus()

A = grafo_grande.get_arestas()

Qtd_arestas = int(len(A)/2)

hist = pd.DataFrame(list(graus.items()), columns=['vertice', 'grau'])

final = hist.groupby('grau').count()

final = final.reset_index()

sns.set_style('darkgrid')
grafico = plt.plot(final.grau, final.vertice)

sns.relplot(x="vertice", y="grau", data = final)