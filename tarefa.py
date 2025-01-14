class Tarefa:
    def __init__(self, identificador, inicio, fim):
        self.id = identificador
        self.inicio = inicio
        self.fim = fim

    def __str__(self):
        return f'{self.id, self.inicio, self.fim}'

    def __repr__(self):
        return self.__str__()