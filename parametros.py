class ParametrosSimulatedAnnealing:
    def __init__(self, alpha, k, temperatura_inicial, temperatura_minima):
        self.alpha = alpha
        self.k = k
        self.temperatura_inicial = temperatura_inicial
        self.temperatura_minima = temperatura_minima

class ParametrosILS:
    def __init__(self, ils_max):
        self.ils_max = ils_max