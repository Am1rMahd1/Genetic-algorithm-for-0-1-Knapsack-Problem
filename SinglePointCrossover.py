from CrossoverOperator import CrossoverOperator


class SinglePointCrossover(CrossoverOperator):
    def crossover(self, parent1, parent2):
        # Single-point crossover implementation
        return