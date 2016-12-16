from collections import defaultdict

class Node:
    """
    Simple node representation.
    """
    
    # The (k-1)mer of the node.
    kmer = ""
    # Identificator, probably useless.
    i = -1
    
    def __init__(self, i, kmer):
        self.kmer = kmer
        self.i = i
    
class Graph:
    """
    Graph represented as a dict.
    Keys: nodes.
    Values: Set of neighbouring nodes - there is one edge between the node (key) and all nodes in a a set (value).
    """
    
    graph = defaultdict(set) # {Node1: (Node2, Node3, Node2), Node2: {Node2, Node1, Node4}}
    
    def find_beginning(self):
        """
        Find the node to begin searching for Euler path with.
        TODO Terrible complexity, would be nice to remember starting node when creating the graph
        and just give it as an argument.
        """
        
        return_node = None
        for node in self.graph:
            return_node = node
            # The number of edges going out from the node.
            out = len(self.graph[node])
            # Compute the number of edges going into the node.
            into = 0
            for neigh in self.graph:
                if node in self.graph[neigh]:
                    into += 1
            # If out > into, we should begin with that node.
            if out > into:
                return node
            
        # All nodes have even degree, the graph is Euler cycle, first node can be whatever node.
        return return_node
                

def load_graph():
    """ Generate simple testing graph. """
    
    g = Graph()
    
    n01 = Node(1, "AB")
    n02 = Node(2, "BC")
    n03 = Node(3, "CD")
    
    n04 = Node(4, "DE")
    n05 = Node(5, "EC")
    
    n06 = Node(6, "DX")
    n07 = Node(7, "XY")
    
    n08 = Node(8, "CE")
    
    g.graph[n01] = set([n02])
    g.graph[n02] = set([n03])
    g.graph[n03] = set([n04, n06])
    g.graph[n04] = set([n05])
    g.graph[n05] = set([n03, n08])
    g.graph[n06] = set([n07])
    g.graph[n08] = set([n05])
    
    # The seqeunce the graph should represent.
    should_be = "ABCDECECDXY"
    
    return (g, should_be)
    
def euler_path(euler_graph):
    """ Find the path in given Euler graph. """
    
    # Init stack of visited nodes and reconstructed sequence.
    stack = []
    path = []
    
    # Find the first node to start with.
    node = euler_graph.find_beginning()
    
    # Go through graph.
    while True:
        if not euler_graph.graph[node]:
            # No more edges going from this node.
            # Append the sequence with the last letter of that node's k-mer.
            path.append(node.kmer[-1])
            if not stack:
                # We went through the whole graph.
                path.append(node.kmer[-2::-1])
                break
            # Take a node from the stack.
            node = stack.pop()
        else:
            # Get random node's neighbour and remove the edge connecting them.
            new_node = euler_graph.graph[node].pop()
            # Add node to the stack.
            stack.append(node)
            # New node is now current node.
            node = new_node
            
    return "".join(path[::-1])

if __name__ == "__main__":
    # Load graph.
    euler_graph, should_be = load_graph()
    # Find sequence (Euler path) in the graph.
    sequence = euler_path(euler_graph)
    print("Found sequence:   %s" % sequence)
    print("Desired sequence: %s" % should_be)