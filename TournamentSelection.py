import random

from SelectionOperator import SelectionOperator


class TournamentSelection(SelectionOperator):
    def select(self, population, fitness):
        tournament_size = 3
        selected = random.sample(population, tournament_size)
        return max(selected, key=lambda ind: fitness(ind))
