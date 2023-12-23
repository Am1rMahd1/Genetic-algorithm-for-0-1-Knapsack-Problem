class KnapsackProblemSolver:
    def __init__(self, max_weight, max_size, items):
        self.max_weight = max_weight
        self.max_size = max_size
        self.items = items

    def is_valid_solution(self, solution):
        total_weight = sum(item.weight for item in solution)
        total_size = sum(item.size for item in solution)
        return total_weight <= self.max_weight and total_size <= self.max_size

    def evaluate_fitness(self, solution):
        if not self.is_valid_solution(solution):
            return 0  # Penalize invalid solutions
        # Fitness evaluation based on knapsack constraints and item values
        return sum(item.value for item in solution)