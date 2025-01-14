from gerador import Gerador
from algoritmos import Algoritmo
from parametros import Parametros

Gerador = Gerador(40)

print(Gerador)

atribuicao_greedy = Algoritmo.greedy(Gerador.equipes, Gerador.tarefas)

print(atribuicao_greedy)

atribuicao_first_improvement = atribuicao_greedy.first_improvement()

print(atribuicao_first_improvement)

parametros = Parametros(alpha=0.9, k=0.1, temperatura_inicial=1, temperatura_minima=0.001)

atribuicao_simulated_annealing = Algoritmo.simulated_annealing(atribuicao_greedy, parametros)

print(atribuicao_simulated_annealing)
