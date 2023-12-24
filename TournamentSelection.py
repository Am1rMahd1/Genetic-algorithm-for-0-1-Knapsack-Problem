import random

from SelectionOperator import SelectionOperator


class TournamentSelection(SelectionOperator):
    def select(self, population, fitness):
        tournament_size = 4
        selected_indices = random.sample(range(len(population)), tournament_size)
        selected_solution = max(selected_indices, key=lambda idx: fitness[idx])
        return population[selected_solution]
