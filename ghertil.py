import heapq


class GhertilHRT:
    def __init__(self, graph):
        self.graph = graph

    def find_path(self, start_node, target_node):
        if start_node not in self.graph or target_node not in self.graph:
            return None, float("pas de solution un des noeuds n'est pas connecte au notre graphe")

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
        current_node = target_node
        while current_node != start_node:
            path.append(current_node)
            current_node = predecessors.get(current_node)
            if current_node is None:
                return None
        path.append(start_node)
        return path[::-1]
