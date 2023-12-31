import random

from MutationOperator import MutationOperator


class BitFlipMutation(MutationOperator):
    def mutate(self, individual):
        mutation_rate = 0.3
        mutated_individual = [
            gene if random.random() > mutation_rate else 1 - gene for gene in individual
        ]
        return mutated_individual
