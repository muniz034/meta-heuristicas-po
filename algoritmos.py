import copy
import math
import random
import time
from copy import deepcopy

from atribuicao import Atribuicao

class Algoritmo:
    @staticmethod
    def greedy(equipes, tarefas):
        atribuicao = Atribuicao()
        atribuicao.equipes = deepcopy(equipes)
        atribuicao.tarefas = deepcopy(tarefas)

        # atribuicao.tarefas.sort(key=lambda x: x.inicio)

        for i in range(len(equipes)):
            atribuicao.equipes[i].tarefas = []

        for i in range(len(tarefas)):
            atribuido = False
            for j in range(len(equipes)):
                atribuicao_valida = True

                for tarefa in atribuicao.equipes[j].tarefas:
                    is_overlaping = tarefa.inicio <= tarefas[i].fim and tarefa.fim >= tarefas[i].inicio
                    if is_overlaping:
                        atribuicao_valida = False
                        break

                if atribuicao_valida:
                    atribuicao.equipes[j].tarefas.append(tarefas[i])
                    atribuido = True
                    break

            if not atribuido:
                print(f"Não foi possível encontrar uma equipe para a tarefa {tarefas[i].id}")

        return atribuicao

    @staticmethod
    def simulated_annealing(atribuicao_inicial, parametros):
        start = time.time()

        # Define s
        s = deepcopy(atribuicao_inicial)

        # Define IterT
        m = len(atribuicao_inicial.equipes)
        n = len(atribuicao_inicial.tarefas)

        n_iteracoes = math.ceil(m * n * parametros.k)

        # Melhor solução obtida até então
        s_estrela = deepcopy(atribuicao_inicial)

        # Temperatura corrente
        temperatura = parametros.temperatura_inicial

        while temperatura > parametros.temperatura_minima:
            for _ in range(n_iteracoes):

                # Gere um vizinho qualquer de s
                s_l = s.random_descent()

                # Define delta
                delta = s_l.custo_total() - s.custo_total()

                if delta < 0:
                    s = s_l
                    if s_l.custo_total() < s_estrela.custo_total():
                        s_estrela = s_l
                else:
                    x = random.random()
                    if x < math.exp(-delta / temperatura):
                        s = s_l

            # Resfriamento
            temperatura *= parametros.alpha

        s = s_estrela

        return round(time.time() - start, 3), s

    @staticmethod
    def ils(atribuicao_inicial, parametros):
        start = time.time()

        # Define s0
        s0 = deepcopy(atribuicao_inicial)

        # Define s
        s = s0.first_improvement()

        # Define Iter, MelhorIter e nivel
        i = 0
        melhor_iter = i
        nivel = 1

        while i - melhor_iter < parametros.ils_max:
            i = i + 1
            s_l = s.pertubacao(nivel)
            s_ll = s_l.first_improvement()

            if s_ll.custo_total() < s.custo_total():
                s = s_ll
                melhor_iter = i
                nivel = 1
            else:
                nivel = nivel + 1

        return round(time.time() - start, 3), s