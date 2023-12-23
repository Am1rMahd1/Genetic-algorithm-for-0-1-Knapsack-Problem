from SelectionOperator import SelectionOperator


class TournamentSelection(SelectionOperator):
    def select(self, population, fitness):
        # Tournament selection implementation
        return