import random


class GeneticAlgorithmSolver:
    def __init__(self, problem_solver, selection_operator=None, crossover_operator=None,
                 mutation_operator=None):
        self.problem_solver = problem_solver
        self.selection_operator = selection_operator
        self.crossover_operator = crossover_operator
        self.mutation_operator = mutation_operator

    def evolve(self, population, children_in_every_generation):
        fitness_scores = [self.problem_solver.evaluate_fitness(chromosome) for chromosome in population]
        selected_population = population if self.selection_operator is None else \
            [population[i] for i in self.selection_operator.select(population, fitness_scores)]

        new_population = []
        while len(new_population) < children_in_every_generation:
            parent1, parent2 = random.sample(selected_population, 2)
            child1, child2 = self.crossover_operator.crossover(parent1, parent2)
            child1 = self.mutation_operator.mutate(child1) if self.mutation_operator else child1
            child2 = self.mutation_operator.mutate(child2) if self.mutation_operator else child2
            new_population.extend([child1, child2])

        return new_population
