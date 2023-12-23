class GeneticAlgorithmSolver:
    def __init__(self, problem_solver, selection_operator, crossover_operator, mutation_operator):
        self.problem_solver = problem_solver
        self.selection_operator = selection_operator
        self.crossover_operator = crossover_operator
        self.mutation_operator = mutation_operator

    def evolve(self, population):
        # Evolution process using the provided operators
        return