from collections import defaultdict


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
            # The number of edges going out from the node.
            out = len(self.graph[node])
            # Compute the number of edges going into the node.
            into = 0
            for neigh in self.graph:
                if node in self.graph[neigh]:
                    into += 1
            # If out > into, we should begin with that node.
            if out > into:
                return_node = node
            
        # All nodes have even degree, the graph is Euler cycle, first node can be whatever node.
        return return_node


def get_kmers(sequence, k):
        for i in range(len(sequence) - (k - 1)):
            yield sequence[i:i+k]

def get_graph(sequence, k):
    g = Graph()
    kmers = get_kmers(sequence, k)
    for kmer in kmers:
        #we add nodes (k-1 mer) and edge in graph : n1 -> n2
        n1 = kmer[:-1]
        n2 = kmer[1:]
        v = g.graph.get(n1, set())
        v.add(n2)
        g.graph[n1] = v

    return g

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
            path.append(node[-1])
            if not stack:
                # We went through the whole graph.
                path.append(node[-2::-1])
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
            
    return "".join(path)[::-1]

if __name__ == "__main__":
    # Load graph.
    euler_graph = get_graph("CATGCATAGCAGAC", 4)
    # Find sequence (Euler path) in the graph.
    sequence = euler_path(euler_graph)
    print("Found sequence:   %s" % sequence)
    print("Desired sequence:  CATGCATAGCAGAC" )
