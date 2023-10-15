class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.weight = 0
        self.edgeCount = 0

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y, w):
        root1 = self.find(x)
        root2 = self.find(y)

        if root1 != root2:
            self.parents[root2] = root1
            self.weight += w
            self.edgeCount += 1

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        edges = [(weight, node1, node2, index) for index, (node1, node2, weight) in enumerate(edges)]
        edges.sort()

        uf1 = UnionFind(n)
        for weight, node1, node2, _ in edges:
            uf1.union(node1, node2, weight)

        minWeight = uf1.weight

        critical_edges = []
        pseudo_critical_edges = []
        m = len(edges)

        for i in range(m):
            uf2 = UnionFind(n)
            for j in range(m):
                if i == j:
                    continue
                w, a, b, _ = edges[j]
                uf2.union(a, b, w)

            if uf2.weight > minWeight or uf2.edgeCount < n - 1:
                critical_edges.append(edges[i][3])
            else:
                uf3 = UnionFind(n)
                weight, node1, node2, _ = edges[i]
                uf3.union(node1, node2, weight)
                for j in range(m):
                    weight, node1, node2, _ = edges[j]
                    uf3.union(node1, node2, weight)

                if uf3.weight == minWeight:
                    pseudo_critical_edges.append(edges[i][3])

        return critical_edges, pseudo_critical_edges