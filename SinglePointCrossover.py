import random

from CrossoverOperator import CrossoverOperator


class SinglePointCrossover(CrossoverOperator):
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, min(len(parent1), len(parent2)) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2
