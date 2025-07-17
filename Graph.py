import networkx as nx
import random
import numpy as np


def create_bipartite_regular(variable, check, dist):
    """
    Creates a d-regular bipartite  graph to generate a tanner code that has optimal parameters.
    variable: Number of variable nodes. Needs to be even.
    check: Number of check nodes.
    dist: Degree for each check node.

    Returns a bipartite regular graph if generated within 100 attempts.
    """
    max_attempt = 100   # Maximum attempts for generating a bipartite regular graph
    attempt = 0

    while attempt < max_attempt:
        attempt += 1
        G = nx.DiGraph()    # Directed graph from networkx
        check_node = []     # List of all check nodes to be added
        variable_node = []  # List of all variable nodes to be added
        success = True

        for j in range(check):
            check_node.append("c" + str(j))
        for i in range(variable):
            variable_node.append("v" + str(i))
        G.add_nodes_from(check_node, bipartite=0)       # Adding nodes
        G.add_nodes_from(variable_node, bipartite=1)

        for c in check_node:    # Creating dist amount of edges for each check node
            available_vars = [v for v in variable_node if not G.has_edge(c, v)]     # Creates a list of all variable nodes the check node can connect to
            temp = random.sample(available_vars, dist)  # Selecting dist amount of variable nodes
            if len(available_vars) < dist:
                success = False
                break

            for j in temp:
                G.add_edge(c, j)

        if success and all(G.degree(c) == dist for c in check_node):    # Checking if all check nodes have degree equal to dist
            return G

    return Exception("Failed to generate a bipartite regular graph")


def generate_biregular_bipartite_graph(n_left, n_right, d_left, d_right, seed=None):
    """
    Randomly generates a (d_left, d_right)-regular bipartite graph to create optimal hypergraph product codes.
    n_left: Number of variable nodes.
    n_right: Number of check nodes.
    d_left: Degree of variable nodes.
    d_right: Degree of check nodes.
    seed: Optional parameter for reproducibility

    Returns a parity matrix generated from the biregular bipartite graph.
    """

    if d_left * n_left != d_right * n_right:    # Initial condition for biregular graphs
        Exception("Size and degree do not match")

    rng = random.Random(seed)

    # Creating a list of left and right nodes
    left_nodes = [f'v{i}' for i in range(n_left)]
    right_nodes = [f'c{j}' for j in range(n_right)]

    # Creating and shuffling half edges to ensure each node has the appropriate degrees
    left_half_edge = [v for v in left_nodes for _ in range(d_left)]
    right_half_edge = [c for c in right_nodes for _ in range(d_right)]
    rng.shuffle(left_half_edge)
    rng.shuffle(right_half_edge)

    # Adding nodes
    G = nx.Graph()
    G.add_nodes_from(left_nodes, bipartite=0)
    G.add_nodes_from(right_nodes, bipartite=1)

    # Pairing half edges and adding them as edges
    for u, v in zip(left_half_edge, right_half_edge):
        G.add_edge(u, v)

    # Convert to parity check matrix in order to use as parameter in ClassicalCode()
    left_nodes.sort()
    right_nodes.sort()
    left_index = {node: j for j, node in enumerate(left_nodes)}
    right_index = {node: i for i, node in enumerate(right_nodes)}

    H = np.zeros((n_right, n_left), dtype=int)

    for u, v in G.edges():  # Generating the parity check matrix according to the graph
        if G.nodes[u]['bipartite'] == 0:
            var, check = u, v
        else:
            var, check = v, u
        i = right_index[check]
        j = left_index[var]
        H[i, j] = 1

    return H