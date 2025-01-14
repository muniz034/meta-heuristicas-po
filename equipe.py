from copy import deepcopy

class Equipe:
    def __init__(self, identificador, custo):
        self.id = identificador
        self.custo = custo
        self.tarefas = []

    """
    Gera representação da grade horária da equipe no formato:
        [0, 0, 0, 1, 1, 1, 0, 0, ...] (24)
    Onde 0 é ausência de tarefa e 1 é existência de tarefa
    E cada indíce é referente a uma unidade de tempo no relógio
    """
    def tabela_tempo(self):
        tempo = [0] * 24
        for i in range(len(self.tarefas)):
            tarefas = deepcopy(self.tarefas)
            tarefas.sort(key=lambda x: x.inicio)

            for j in range(len(tarefas)):
                tarefa = tarefas[j]
                tempo[tarefa.inicio] = 1
                tempo[tarefa.inicio + 1] = 1
                tempo[tarefa.inicio + 2] = 1

        return tempo

    def __str__(self):
        return f'{self.id}'

    def __repr__(self):
        return self.__str__()
