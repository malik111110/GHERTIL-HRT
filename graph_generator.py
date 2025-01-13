import random


class GraphGenerator:
    def __init__(self, num_nodes=10, min_edges=1, max_edges=1):
        self.num_nodes = num_nodes
        self.min_edges = min_edges
        self.max_edges = max_edges

    def generate(self):
        graph = {i: {} for i in range(self.num_nodes)}
        for node in range(self.num_nodes-5):
            num_edges = random.randint(self.min_edges, self.max_edges)
            neighbors = random.sample(
                [n for n in range(self.num_nodes) if n != node], num_edges
            )
            for neighbor in neighbors:
                cost = random.randint(1, 10)
                graph[node][neighbor] = cost
                graph[neighbor][node] = cost  # Graphe non orienté
        return graph
