class Graph:
    def __init__(self, num_nodes: int, edge_list: List[List[int]]):
        self.graph = defaultdict(dict)
        for node_a, node_b, edge_cost in edge_list:
            self.graph[node_a][node_b] = edge_cost

    def addEdge(self, edge_data: List[int]) -> None:
        node_a, node_b, edge_cost = edge_data
        self.graph[node_a][node_b] = edge_cost

    def shortestPath(self, start_node: int, end_node: int) -> int:
        graph, seen = self.graph, set()
        heap = [(0, start_node)]
        while heap:
            total_cost, current_node = heappop(heap)
            if current_node == end_node:
                return total_cost
            if current_node not in seen and current_node in graph:
                seen.add(current_node)
                for neighbor, edge_cost in graph[current_node].items():
                    heappush(heap, (total_cost + edge_cost, neighbor))
        return -1
