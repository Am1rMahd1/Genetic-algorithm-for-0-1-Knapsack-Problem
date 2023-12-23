from BitFlipMutation import BitFlipMutation
from GeneticAlgorithmSolver import GeneticAlgorithmSolver
from KnapsackItem import KnapsackItem
from KnapsackProblemSolver import KnapsackProblemSolver
from SinglePointCrossover import SinglePointCrossover
from TournamentSelection import TournamentSelection

max_weight = 220
max_size = 2

items = [
    KnapsackItem(weight=55, size=0.03, value=11),
    KnapsackItem(weight=67, size=0.12, value=97),
    KnapsackItem(weight=87, size=0.34, value=34),
    KnapsackItem(weight=29, size=0.38, value=30),
    KnapsackItem(weight=67, size=0.21, value=47),
    KnapsackItem(weight=32, size=0.16, value=31),
    KnapsackItem(weight=7, size=0.25, value=12),
    KnapsackItem(weight=14, size=0.32, value=9),
    KnapsackItem(weight=52, size=0.86, value=98),
    KnapsackItem(weight=33, size=0.30, value=54),
    KnapsackItem(weight=72, size=0.72, value=59),
    KnapsackItem(weight=51, size=0.93, value=71),
    KnapsackItem(weight=94, size=1.1, value=43),
    KnapsackItem(weight=102, size=0.35, value=28),
    KnapsackItem(weight=21, size=0.58, value=56),
    KnapsackItem(weight=28, size=0.46, value=87),
    KnapsackItem(weight=8, size=0.15, value=21),
    KnapsackItem(weight=58, size=0.32, value=16),
    KnapsackItem(weight=9, size=0.29, value=30),
    KnapsackItem(weight=46, size=0.03, value=5),
    KnapsackItem(weight=23, size=0.01, value=11),
    KnapsackItem(weight=13, size=0.76, value=39),
    KnapsackItem(weight=19, size=0.54, value=75),
    KnapsackItem(weight=19, size=0.72, value=31),
    KnapsackItem(weight=70, size=0.26, value=19),
    KnapsackItem(weight=42, size=0.11, value=53),
    KnapsackItem(weight=60, size=0.30, value=70),
    KnapsackItem(weight=37, size=0.65, value=45),
    KnapsackItem(weight=22, size=0.43, value=69),
]

problem_solver = KnapsackProblemSolver(max_weight, max_size, items)
selection_op = TournamentSelection()
crossover_op = SinglePointCrossover()
mutation_op = BitFlipMutation()

genetic_solver = GeneticAlgorithmSolver(problem_solver, selection_op, crossover_op, mutation_op)
initial_population = [...]
final_population = genetic_solver.evolve(initial_population)
