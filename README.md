# README: GHERTIL HRT Algorithm (Non-Markovian Version)

## Introduction

The **GHERTIL HRT** algorithm is a dynamic pathfinding algorithm designed to find the shortest path between two nodes in a weighted graph. It employs a priority queue to explore nodes based on their current distances and reconstructs the optimal path using a predecessor map. This version does not incorporate Markov probabilistic models, making it deterministic and suitable for simpler use cases.

## Key Features

- **Deterministic Pathfinding**: Finds the shortest path between a start node and a target node in a weighted graph.
- **Dynamic State Exploration**: Dynamically updates node distances during traversal.
- **Simple and Efficient**: Uses a priority queue (min-heap) for efficient node selection.

## Algorithm Description

1. **Initialization**:

   - Set the distance of all nodes to infinity (`float("inf")`), except the start node, which is set to 0.
   - Initialize a priority queue with the start node.
   - Create a predecessor map to reconstruct the shortest path.

2. **Traversal**:

   - While the priority queue is not empty, extract the node with the smallest distance.
   - For each neighbor of the current node, calculate the tentative distance. If it is smaller than the currently known distance, update it and push the neighbor to the queue.

3. **Path Reconstruction**:

   - Once the target node is reached, reconstruct the path using the predecessor map.

4. **Output**:

   - Return the shortest path and its total cost. If no path exists, return `None` and infinity (`float("inf")`).

## Implementation

```python
import heapq

class GhertilHRT:
    def __init__(self, graph):
        self.graph = graph

    def find_path(self, start_node, target_node):
        if start_node not in self.graph or target_node not in self.graph:
            return None, "No solution: one of the nodes is not connected to the graph"

        distances = {node: float("inf") for node in self.graph}
        distances[start_node] = 0
        priority_queue = [(0, start_node)]
        predecessors = {}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == target_node:
                path = self.reconstruct_path(predecessors, start_node, target_node)
                return path, current_distance

            for neighbor, cost in self.graph[current_node].items():
                distance = current_distance + cost
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return None, float("inf")

    def reconstruct_path(self, predecessors, start_node, target_node):
        path = []
        current = target_node
        while current != start_node:
            path.append(current)
            current = predecessors[current]
        path.append(start_node)
        path.reverse()
        return path
```

## Example Usage

### Input Graph

```python
example_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
```

### Example

```python
from ghertil_hrt import GhertilHRT

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

algorithm = GhertilHRT(graph)
path, cost = algorithm.find_path('A', 'D')
print("Path:", path)
print("Cost:", cost)
```

### Output

```
Path: ['A', 'B', 'C', 'D']
Cost: 4
```

## Complexity

### Time Complexity

- **Best Case**: O(E + V log V) where E is the number of edges, and V is the number of vertices.
- **Worst Case**: O(E log V), assuming a dense graph where all nodes are interconnected.

### Space Complexity

- O(V + E), for storing the graph, distances, predecessors, and priority queue.

## Potential Applications

- **Networking**: Routing and packet forwarding in computer networks.
- **Transportation**: Finding the shortest route in navigation systems.
- **Game Development**: Pathfinding in virtual environments.
- **Operations Research**: Optimizing logistics and supply chain management.

## Comparisons with Dijkstra and A\*

### Similarities

- Both Dijkstra and GHERTIL HRT use a priority queue (min-heap) to find the shortest path.
- They explore nodes based on the current known shortest distance.

### Differences

- **Dijkstra's Algorithm**: Assumes a uniform exploration process, treating all nodes equally. GHERTIL HRT includes an additional mechanism for path reconstruction, streamlining certain applications.
- **A**\*: Uses a heuristic to guide its search, making it more efficient for certain problems (like grids with defined goals). GHERTIL HRT lacks heuristics, making it deterministic but potentially slower for certain use cases.

### Complexity Comparison

#### Time Complexity

- **Dijkstra**: O(E + V log V) in its most efficient implementation.
- **A**\*: O(E + V log V), but can vary depending on the heuristic.
- **GHERTIL HRT**: O(E + V log V) in most cases, with additional time for path reconstruction.

#### Space Complexity

- **Dijkstra**: O(V + E), as it stores distances and predecessors.
- **A**\*: O(V + E + heuristic storage).
- **GHERTIL HRT**: O(V + E), similar to Dijkstra.

### When to Use

- **GHERTIL HRT**: Best for scenarios where simplicity and deterministic paths are sufficient (e.g., logistics planning, routing in dynamic networks).
- **Dijkstra**: Suitable for graphs with uniform cost distributions.
- **A**\*: Ideal for spatial pathfinding where heuristics can be applied (e.g., gaming and robotics).

## Limitations

- Assumes all edge weights are non-negative.
- Performance may degrade for extremely large graphs.

## License

This implementation of the GHERTIL HRT Algorithm is open source. Feel free to use and modify it in your projects.

