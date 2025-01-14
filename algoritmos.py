import copy
import math
import random
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
        atribuicao_inicial = deepcopy(atribuicao_inicial)

        m = len(atribuicao_inicial.equipes)
        n = len(atribuicao_inicial.tarefas)

        n_iteracoes = math.ceil(m * n * parametros.k)

        temperatura = parametros.temperatura_inicial

        s_l = atribuicao_inicial
        custo_atual = s_l.custo_total()

        melhor_solucao = deepcopy(s_l)
        melhor_custo = custo_atual

        while temperatura > parametros.temperatura_minima:
            for _ in range(n_iteracoes):
                vizinho = s_l.first_improvement()

                custo_vizinho = vizinho.custo_total()

                delta = custo_vizinho - custo_atual

                x = random.random()

                if delta < 0 or x < math.exp(-delta / temperatura):
                    s_l = vizinho
                    custo_atual = custo_vizinho

                    # Atualizar a melhor solução
                    if custo_atual < melhor_custo:
                        melhor_solucao = s_l
                        melhor_custo = custo_atual

            temperatura *= parametros.alpha  # Resfriamento
            # print(f"R${melhor_custo} : {temperatura}")

        return melhor_solucao