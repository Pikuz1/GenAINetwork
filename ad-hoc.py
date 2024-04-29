import random
import networkx as nx
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms
from scipy.spatial import distance

# Create a random ad hoc network
def create_adhoc_network(num_nodes, max_distance):
    G = nx.Graph()
    for node in range(num_nodes):
        G.add_node(node, pos=(random.uniform(0, max_distance), random.uniform(0, max_distance)))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 != node2:
                pos1 = G.nodes[node1]['pos']
                pos2 = G.nodes[node2]['pos']
                dist = distance.euclidean(pos1, pos2)
                if dist <= max_distance:
                    G.add_edge(node1, node2, weight=dist)
    return G

# Fitness function: minimize total distance
def evaluate(individual, graph):
    total_distance = 0
    # Check if the path is valid
    if len(individual) < 2:
        return (float('inf'),)  # Return infinity as a tuple for invalid paths

    for i in range(len(individual) - 1):
        # Check if the edge exists in the graph
        if not graph.has_edge(individual[i], individual[i + 1]):
            return (float('inf'),)  # Return infinity as a tuple for invalid paths
        total_distance += graph.edges[individual[i], individual[i + 1]]['weight']
    return (total_distance,)  # Return the total distance as a single-element tuple

# Calculate average fitness safely for both floats and sequences
def safe_avg(x):
    if isinstance(x, (int, float)):
        return x
    elif isinstance(x, tuple):  # Check if x is a tuple
        return x[0]  # Unpack the tuple and return the first element (assuming it's a single value)
    elif isinstance(x, (list,)):  # Check if x is a list
        if len(x) > 0:
            return sum(x) / len(x)  # Calculate average for non-empty list
        else:
            return float('nan')  # Return NaN for empty list
    else:
        raise TypeError("Unsupported type for safe_avg")

# Genetic Algorithm parameters
NUM_NODES = 10
MAX_DISTANCE = 10
POP_SIZE = 100
CXPB = 0.7
MUTPB = 0.2
NUM_GEN = 100

# Create the ad hoc network graph
graph = create_adhoc_network(NUM_NODES, MAX_DISTANCE)

# Create the individual and population
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)
toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(NUM_NODES), NUM_NODES)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate, graph=graph)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Initialize the population
population = toolbox.population(n=POP_SIZE)

# Create the statistics object and register functions
stats = tools.Statistics(key=lambda ind: ind.fitness.values)
stats.register("avg", safe_avg)
stats.register("min", min)
stats.register("max", max)

# Run the genetic algorithm with statistics
population, logbook = algorithms.eaSimple(population, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=NUM_GEN, stats=stats, verbose=True)

# Extract the best individual
best_individual = tools.selBest(population, k=1)[0]
best_path_indices = best_individual  # Assuming the best individual is a list of node indices

# Example mapping of node indices to node names
node_names_map = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
    5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'  # Add more nodes as needed
}

# Assuming best_path_indices contains the indices of nodes in the best path
best_path_indices = [0, 1, 3, 2]  # Example indices (replace with your actual indices)

# Convert node indices to node names in the best path
best_path_names = [node_names_map[node_index] for node_index in best_path_indices]

# Print the node names along with the shortest path found
print("Shortest Path Nodes:")
print(best_path_names)


# Print the best path length
best_path_length = best_individual.fitness.values[0] if len(best_individual.fitness.values) > 0 else float('nan')
print("Best Path Length:", best_path_length)
