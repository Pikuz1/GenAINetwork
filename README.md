# Genetic Algorithm for Shortest Path in Ad Hoc Network

## Overview

This Python script demonstrates the implementation of a genetic algorithm to find the shortest path in a wireless ad hoc network. It uses the DEAP (Distributed Evolutionary Algorithms in Python) library for genetic programming and optimization.

## Setup

### Dependencies

- Python 3.x
- NetworkX: `pip install networkx`
- Matplotlib: `pip install matplotlib`
- DEAP: `pip install deap`
- SciPy: `pip install scipy`

### Usage

1. Clone the repository or download the script.
2. Install dependencies as mentioned above.
3. Run the script: `python genetic_algorithm_shortest_path.py`

## Code Explanation

- `create_adhoc_network`: Function to create a random ad hoc network using NetworkX.
- `evaluate`: Fitness function to minimize total distance in the network.
- `safe_avg`: Function to calculate average fitness safely for both single values and tuples.
- Genetic Algorithm Parameters: NUM_NODES, MAX_DISTANCE, POP_SIZE, CXPB, MUTPB, NUM_GEN.
- Creation of DEAP components: Fitness, Individual, Toolbox, Statistics.
- Initialization of the population and registration of genetic operators (mate, mutate, select).
- Run the genetic algorithm using `algorithms.eaSimple` with statistics.
- Extract the best individual and convert node indices to node names in the best path.

## Output

- The script will output the nodes along with the shortest path found in the ad hoc network.
- It will also print the length of the best path found.

## Additional Notes

- Modify the `node_names_map` dictionary to match your actual node indices to node names mapping.
- Adjust the `best_path_indices` variable with your actual indices of nodes in the best path.

Feel free to modify the code as needed for your specific ad hoc network or optimization problem.

For any questions or issues, please contact [priyankagiri.oyeindia@gmail.com].

