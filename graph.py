from collections import deque
from heapq import heappop

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.edges = []

class Graph:
    def __init__(self) -> None:
        self.nodes = {}

    def add_node(self, value):
        new_node = Node(value)
        self.nodes[value] = new_node

    def add_edge(self, source, dest):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)

        self.nodes[source].edges.append(dest)

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])

        while queue:
            selected_node = queue.popleft()

            if selected_node not in visited:
                visited.add(selected_node)
                
                for neighbor in selected_node.edges:
                    queue.append(self.nodes[neighbor])

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]

        while stack:
            selected_node = stack.pop()

            if selected_node not in visited:
                visited.add(selected_node)
                
                for neighbor in selected_node.edges:
                    stack.append(self.nodes[neighbor])

    def dijkstra(self, start_node):
        unvisited = set(self.nodes.keys())
        distances = {node: float("inf") for node in unvisited}
        distances[start_node] = 0

        while unvisited:
            min_distance_node = min(unvisited, key=distances.get)
            unvisited.remove(min_distance_node)
            current_node = self.nodes[min_distance_node]

            for neighbor in current_node.edges:
                tentative_distance = distances[min_distance_node] + 1
                
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance

    def prim(self):
        """
        Implements Prim's algorithm for finding the minimum spanning tree.
        """
        visited = set()
        mst = []  # Minimum spanning tree edges
        current_node = next(iter(self.nodes.values()))  # Pick any starting node
        visited.add(current_node.value)

        while len(visited) != len(self.nodes):
            min_edge = (float("inf"), None, None)  # (weight, source, destination)
            for node in visited:
                for neighbor in self.nodes[node].edges:
                    if neighbor not in visited and self.nodes[node].value not in [min_edge[1], min_edge[2]]:
                        weight = 1  # Assuming edge weight of 1
                        if weight < min_edge[0]:
                            min_edge = (weight, node, neighbor)
            visited.add(min_edge[2])
            mst.append((min_edge[0], min_edge[1], min_edge[2]))

        print("Minimum Spanning Tree:", mst)

    def bellman_ford(self, start_node):
        """
        Implements Bellman-Ford algorithm for finding the shortest paths.
        """
        distances = {node: float("inf") for node in self.nodes}
        distances[start_node] = 0

        # Relax all edges V-1 times
        for _ in range(len(self.nodes) - 1):
            for source in self.nodes:
                for neighbor in self.nodes[source].edges:
                    new_distance = distances[source] + 1  # Assuming edge weight of 1
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

        # Check for negative weight cycles
        for source in self.nodes:
            for neighbor in self.nodes[source].edges:
                new_distance = distances[source] + 1
                if new_distance < distances[neighbor]:
                    print("Negative weight cycle detected!")
                    return

        print("Shortest distances from", start_node, ":", distances)

graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "E")
graph.add_edge("A", "E")

graph.bellman_ford("A")
graph.dijkstra("A")
graph.prim()

