import copy
from copy import deepcopy
import random
from datetime import datetime

class Atribuicao:
    def __init__(self, equipes=None, tarefas=None):
        if tarefas is None:
            tarefas = []

        if equipes is None:
            equipes = []

        self.equipes = equipes
        self.tarefas = tarefas

    """
    Levando em consideração que todas tarefas tem 3h de duração
    """
    def custo_total(self):
        custo = 0
        for i in range(len(self.equipes)):
            custo = custo + self.equipes[i].custo * (len(self.equipes[i].tarefas) * 3)
        return custo

    def busca_equipe(self, tempo_inicial):
        equipes = []
        for i in range(len(self.equipes)):
            tarefas = self.equipes[i].tarefas
            for j in range(len(tarefas)):
                if tarefas[j].inicio == tempo_inicial:
                    equipes.append(self.equipes[i])
                    break
        return equipes

    def first_improvement(self):
        atribuicao_atual = copy.deepcopy(self)

        realoca = False

        # Realoca se possível
        for i in range(len(atribuicao_atual.equipes)):
            equipe = atribuicao_atual.equipes[i]

            if realoca:
                break

            time = equipe.tabela_tempo()

            for j in range(len(time) - 2):
                if realoca:
                    break

                if time[j] == 0 and time[j + 1] == 0 and time[j + 2] == 0:
                    for k in range(len(atribuicao_atual.equipes)):
                        if realoca:
                            break

                        if k != i:
                            tarefas = atribuicao_atual.equipes[k].tarefas

                            for l in range(len(tarefas)):
                                if realoca:
                                    break

                                tarefa = tarefas[l]
                                # Posso checar tambem se i tem um custo por hora menor que k
                                if tarefa.inicio == j and atribuicao_atual.equipes[i].custo < atribuicao_atual.equipes[k].custo:
                                    atribuicao_atual.equipes[i].tarefas.append(tarefa)
                                    atribuicao_atual.equipes[k].tarefas.pop(l)
                                    realoca = True

        return atribuicao_atual

    def random_descent(self):
        random.seed(datetime.now().timestamp())

        atribuicao_atual = copy.deepcopy(self)

        realoca = False
        n = 0

        while realoca == False and n < 1000:
            i = random.randint(0, len(atribuicao_atual.equipes) - 1)

            equipe = atribuicao_atual.equipes[i]

            time = equipe.tabela_tempo()

            for j in range(len(time) - 2):
                if realoca:
                    break

                if time[j] == 0 and time[j + 1] == 0 and time[j + 2] == 0:
                    equipes = atribuicao_atual.busca_equipe(j)

                    # print(equipes)

                    if len(equipes) == 0:
                        continue

                    k = random.randint(0, len(equipes) - 1)
                    index, tarefa = equipes[k].busca_tarefa(j)

                    atribuicao_atual.equipes[i].tarefas.append(tarefa)
                    equipes[k].tarefas.pop(index)
                    # print(f"Passa tarefa {tarefa} da equipe {equipes[k]} para a equipe {equipe}")
                    realoca = True

        return atribuicao_atual

    def pertubacao(self, nivel):
        s_l = deepcopy(self)
        n_modificacoes = nivel + 1
        cont = 1

        while cont <= n_modificacoes:
            s_l = s_l.random_descent()
            cont = cont + 1

        return s_l

    def __str__(self):
        result = "Atribuições: \n"

        for i in range(len(self.equipes)):
            equipe = self.equipes[i]
            result = result + f"\tEquipe {equipe.id}: " + str(equipe.tarefas) + "\n"

        result += f"Custo Total: R${round(self.custo_total(), 2)}"

        return result

    def __repr__(self):
        return self.__str__()