from gerador import Gerador
from algoritmos import Algoritmo
from parametros import ParametrosSimulatedAnnealing, ParametrosILS

tarefas = Gerador.parse_tarefas([(0, 10, 12), (1, 0, 2), (2, 5, 7), (3, 16, 18), (4, 3, 5), (5, 2, 4), (6, 19, 21), (7, 17, 19), (8, 9, 11), (9, 14, 16), (10, 2, 4), (11, 9, 11), (12, 3, 5), (13, 3, 5), (14, 19, 21), (15, 7, 9), (16, 1, 3), (17, 9, 11), (18, 19, 21), (19, 15, 17), (20, 5, 7), (21, 9, 11), (22, 18, 20), (23, 0, 2), (24, 6, 8), (25, 3, 5), (26, 5, 7), (27, 14, 16), (28, 11, 13), (29, 9, 11), (30, 9, 11), (31, 16, 18), (32, 7, 9), (33, 17, 19), (34, 17, 19), (35, 15, 17), (36, 11, 13), (37, 10, 12), (38, 6, 8), (39, 4, 6), (40, 15, 17), (41, 8, 10), (42, 2, 4), (43, 17, 19), (44, 9, 11), (45, 8, 10), (46, 19, 21), (47, 0, 2), (48, 5, 7), (49, 9, 11), (50, 8, 10), (51, 0, 2), (52, 13, 15), (53, 17, 19), (54, 1, 3), (55, 11, 13), (56, 2, 4), (57, 0, 2), (58, 5, 7), (59, 15, 17), (60, 8, 10), (61, 1, 3), (62, 9, 11), (63, 9, 11), (64, 10, 12), (65, 8, 10), (66, 2, 4), (67, 11, 13), (68, 7, 9), (69, 12, 14), (70, 8, 10), (71, 12, 14), (72, 10, 12), (73, 19, 21), (74, 11, 13), (75, 9, 11), (76, 6, 8), (77, 3, 5), (78, 1, 3), (79, 16, 18), (80, 17, 19), (81, 13, 15), (82, 9, 11), (83, 8, 10), (84, 16, 18), (85, 7, 9), (86, 2, 4), (87, 7, 9), (88, 12, 14), (89, 13, 15), (90, 12, 14), (91, 13, 15), (92, 3, 5), (93, 3, 5), (94, 12, 14), (95, 7, 9), (96, 15, 17), (97, 20, 22), (98, 19, 21), (99, 7, 9), (100, 14, 16), (101, 5, 7), (102, 7, 9), (103, 6, 8), (104, 18, 20), (105, 13, 15), (106, 6, 8), (107, 13, 15), (108, 0, 2), (109, 14, 16), (110, 9, 11), (111, 18, 20), (112, 15, 17), (113, 20, 22), (114, 14, 16), (115, 1, 3), (116, 14, 16), (117, 10, 12), (118, 19, 21), (119, 18, 20)])
equipes = Gerador.parse_equipes([0.858, 0.767, 0.27, 0.566, 0.645, 0.94, 0.196, 0.715, 0.799, 0.368, 0.831, 0.709, 0.763, 0.738, 0.537, 0.496, 0.681, 0.521, 0.157, 0.344, 0.696, 0.592, 0.067, 0.966, 0.426, 0.851, 0.565, 0.392, 0.291, 0.892])

atribuicao_greedy = Algoritmo.greedy(equipes, tarefas)

for alpha in [0.8, 0.9, 0.95]:
    parametros = ParametrosSimulatedAnnealing(alpha, k=0.1, temperatura_inicial=1, temperatura_minima=0.0001)
    for _ in range(10):
        elapsed, atribuicao_simulated_annealing = Algoritmo.simulated_annealing(atribuicao_greedy, parametros)
        print(f"{_}\t{elapsed}\t{atribuicao_simulated_annealing.custo_total()}")
    print()

for ils_max in [10, 20, 40, 80, 160]:
    for _ in range(10):
        elapsed, atribuicao_ils = Algoritmo.ils(atribuicao_greedy, ParametrosILS(ils_max))
        print(f"{_}\t{elapsed}\t{atribuicao_ils.custo_total()}")
    print()