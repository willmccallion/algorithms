import random
import sys

class graphNode:
    def __init__(self, index):
        self.index = index
        self.colour = "WHITE"
        self.predec = None
        self.dtime = None
        self.ftime = None

    def printNode(self):
        print("Index: ", self.index)
        print("Colour: ", self.colour)
        if self.predec != None:
            print("Predec: ", self.predec.index)
        print("dtime: ", self.dtime)
        print("ftime: ", self.ftime)
        print("--------------------")

    def printPredec(self):
        if self.predec != None:
            print(f"Index: {self.index} was visted from: {self.predec}")

def print_graph(adjacencyList: dict):
    for key, neighbors in adjacencyList.items():
        neighbor_indices = [neighbor.index for neighbor in neighbors]
        print(f"Node {key} is connected to: {neighbor_indices}")

global time
global adjacencyList

def DFS(G: list) -> None:
    global time
    time = 0
    for v in G:
        if v.colour == "WHITE":
            DFS_visit(G,v)


def DFS_visit(G: list, s: graphNode) -> None:
    global time
    global adjacencyList
    s.colour = "GRAY"
    time = time + 1
    s.dtime = time
    for u in adjacencyList[s.index]:
        if u.colour == "WHITE":
            u.predec = s
            DFS_visit(G,u)
    s.colour = "BLACK"
    time = time + 1
    s.ftime = time


def create_random_graph(n: int, edge_probability: float, directed: bool = True):
    global adjacencyList
    nodes = {}
    adjacencyList = {}
    
    for i in range(1, n + 1):
        key = str(i)
        nodes[key] = graphNode(key)
        adjacencyList[key] = []
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                if random.random() < edge_probability:
                    adjacencyList[str(i)].append(nodes[str(j)])
                    if not directed:
                        adjacencyList[str(j)].append(nodes[str(i)])
    
    return nodes, adjacencyList

if __name__ == "__main__":
    nodes, adjacencyList = create_random_graph(int(sys.argv[1]), edge_probability=0.5, directed=True)
    
    G = list(nodes.values())
    DFS(G)

    print_graph(adjacencyList)
    
    for node in G:
        node.printPredec()
        assert(node.colour == "BLACK")

    print("All nodes checked.")