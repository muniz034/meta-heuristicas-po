import copy

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

    def __str__(self):
        result = "Atribuições: \n"

        for i in range(len(self.equipes)):
            equipe = self.equipes[i]
            result = result + f"\tEquipe {equipe.id}: " + str(equipe.tarefas) + "\n"

        result += f"Custo Total: R${self.custo_total()}"

        return result

    def __repr__(self):
        return self.__str__()