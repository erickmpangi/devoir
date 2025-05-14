from collections import defaultdict
import sys
sys.setrecursionlimit(10000)  # si le graphe est profond

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.index = 0
        self.indexes = [-1] * (V + 1)
        self.lowlink = [-1] * (V + 1)
        self.on_stack = [False] * (V + 1)
        self.stack = []
        self.SCCs = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def strongconnect(self, v):
        self.indexes[v] = self.lowlink[v] = self.index
        self.index += 1
        self.stack.append(v)
        self.on_stack[v] = True

        for w in self.graph[v]:
            if self.indexes[w] == -1:
                self.strongconnect(w)
                self.lowlink[v] = min(self.lowlink[v], self.lowlink[w])
            elif self.on_stack[w]:
                self.lowlink[v] = min(self.lowlink[v], self.indexes[w])

        if self.lowlink[v] == self.indexes[v]:
            scc = []
            while True:
                w = self.stack.pop()
                self.on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            self.SCCs.append(sorted(scc))

    def tarjans(self):
        for v in range(1, self.V + 1):
            if self.indexes[v] == -1:
                self.strongconnect(v)
        return self.SCCs


# Lecture de l'entrée
def main():
    V, E = map(int, input().split())
    g = Graph(V)
    for _ in range(E):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    SCCs = g.tarjans()
    SCCs.sort(key=lambda x: x[0])  # trier par plus petit sommet

    print(len(SCCs))
    for comp in SCCs:
        print(" ".join(map(str, comp)))

# Exemple d’utilisation
if __name__ == "__main__":
    main()



