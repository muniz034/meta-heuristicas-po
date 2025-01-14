import random
import math
from datetime import datetime

from equipe import Equipe
from tarefa import Tarefa

random.seed(datetime.now().timestamp())

class Gerador:
    def __init__(self, n_tarefas):
        self.n_tarefas = n_tarefas
        self.n_equipes = math.ceil(n_tarefas / 3)
        self.equipes = []
        self.tarefas = []
        self.gera_equipes()
        self.gera_tarefas()

    def gera_equipes(self):
        for i in range(self.n_equipes):
            custo_por_hora = round(random.random(), 3)
            equipe = Equipe(i, custo_por_hora)
            self.equipes.append(equipe)

    def gera_tarefas(self):
        for i in range(self.n_tarefas):
            inicio = random.randint(0, 20)
            self.tarefas.append(Tarefa(i, inicio, inicio + 2))

    @staticmethod
    def parse_tarefas(t):
        tarefas = []
        for tarefa in t:
            tarefas.append(Tarefa(tarefa[0], tarefa[1], tarefa[2]))

        return tarefas

    @staticmethod
    def parse_equipes(e):
        equipes = []
        for i in range(len(e)):
            equipes.append(Equipe(i, e[i]))

        return equipes

    def __str__(self):
        custos = []

        for equipe in self.equipes:
            custos.append(equipe.custo)

        return f"[{len(self.tarefas)}] {custos} {self.tarefas}"