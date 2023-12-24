# Solve 0-1 Knapsack using Genetic Algorithm

This readme file provides an overview of a Python program that aims to solve the [0-1 Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem) using the [Genetic Algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm). The program follows the principles of [SOLID](https://en.wikipedia.org/wiki/SOLID) to ensure clean and maintainable code.

## Genetic Algorithm Components

The Genetic Algorithm in this scenario consists of the following components:

1. Selection Operator: Tournament Selection is used as the selection operator.
2. Crossover Operator: Single Point Crossover is used as the crossover operator.
3. Mutation Operator: Bit Flip Mutation is used as the mutation operator.

## Considered Attributes

In the 0-1 Knapsack problem implemented in this program, the following attributes are considered for each item:

- Weight
- Size
- Value

## Installation

To install the required dependencies, please use the package manager [pip](https://pip.pypa.io/en/stable/) and run the following command:

```bash
pip install -r .\\requirements.txt
```

## Contributing

Contributions in the form of pull requests are welcome. If you plan to make major changes, please open an issue first to discuss the proposed modifications.

## License

This program is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).