import random
import sys

class graphNode:
    def __init__(self, index):
        self.index = index
        self.colour = "WHITE"
        self.predec = None
        self.dist = None

    def printNode(self):
        print("Index: ", self.index)
        print("Colour: ", self.colour)
        if self.predec != None:
            print("Predec: ", self.predec.index)
        if self.dist != None:
            print("Distance: ", self.dist)
        print("--------------------")

    def printPredec(self):
        if self.predec != None:
            print(f"Index: {self.index} was visted from: {self.predec}")

def print_graph(adjacencyList: dict):
    for key, neighbors in adjacencyList.items():
        neighbor_indices = [neighbor.index for neighbor in neighbors]
        print(f"Node {key} is connected to: {neighbor_indices}")

global adjacencyList

def BFS(G: list) -> None:
    for v in G:
        if v.colour == "WHITE":
            BFS_visit(G,v)

def BFS_visit(G,s):
    queue = []
    s.colour = "GRAY"
    s.dist = 0
    queue.append(s)
    while len(queue) != 0:
        u = queue.pop(0)
        for v in adjacencyList[u.index]:
            if v.colour == "WHITE":
                v.colour = "GRAY"
                v.dist = u.dist + 1
                v.predec = u
                queue.append(v)
    
        u.colour = "BLACK"

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
    BFS(G)

    print_graph(adjacencyList)
    
    for node in G:
        node.printNode()
        node.printPredec()
        assert(node.colour == "BLACK")

    print("All nodes checked.")