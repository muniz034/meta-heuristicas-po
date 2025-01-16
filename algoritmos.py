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

        qtd_vezes_aceita = 0

        # print(f"\nIniciando Simulated Annealing com os parametros: ")
        # print(f"\t Temperatura Inicial: {temperatura}")
        # print(f"\t Temperatura Final: {parametros.temperatura_minima}")
        # print(f"\t Nº de Iterações por Temperatura: {n_iteracoes}\n")

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
                        qtd_vezes_aceita = qtd_vezes_aceita + 1
                        s = s_l

            # Resfriamento
            temperatura *= parametros.alpha

        s = s_estrela

        # print(f"\nTask Count: {len(atribuicao_inicial.tarefas)}")
        # print(f"Time Elapsed: {round(time.time() - start, 3)}s")
        # print(f"Initial Cost: R${round(atribuicao_inicial.custo_total(), 2)}")
        # print(f"Final Cost: R${round(s.custo_total(), 2)}")

        return round(time.time() - start, 3), s