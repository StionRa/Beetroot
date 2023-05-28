from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.scc_list = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, low, disc, stack, in_stack):
        static_time = 0
        disc[v] = static_time
        low[v] = static_time
        static_time += 1
        stack.append(v)
        in_stack[v] = True

        for neighbor in self.graph[v]:
            if disc[neighbor] == -1:
                self.DFSUtil(neighbor, low, disc, stack, in_stack)
                low[v] = min(low[v], low[neighbor])
            elif in_stack[neighbor]:
                low[v] = min(low[v], disc[neighbor])

        if low[v] == disc[v]:
            scc = []
            while True:
                node = stack.pop()
                scc.append(node)
                in_stack[node] = False
                if node == v:
                    break
            self.scc_list.append(scc)

    def getSCCs(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        stack = []
        in_stack = [False] * self.V

        for v in range(self.V):
            if disc[v] == -1:
                self.DFSUtil(v, low, disc, stack, in_stack)

        return self.scc_list


# Creating a graph of 8 vertices
g = Graph(8)
# Rib additions
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

# Obtaining strongly bonded components
scc_list = g.getSCCs()

# Obtaining strongly bonded components
print("Strongly Connected Components:")
for scc in scc_list:
    print(scc)
