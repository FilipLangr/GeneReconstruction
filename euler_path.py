from collections import defaultdict

class Graph:
    """
    Graph represented as a dict.
    Keys: kmers (string).
    Values: List of neighbouring kmers (string).
    """
    
    graph = defaultdict(set)
    
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
                into += sum(1 for kmer in self.graph[neigh] if kmer == node)
            # If out > into, we should begin with that node.
            if out > into:
                return return_node
            
        # All nodes have even degree, the graph is Euler cycle, first node can be whatever node.
        return return_node
    
    def __str__(self):
        return 30*"=" + "\nGraph:\n" + "\n".join(item + ": " + " ".join(item for item in euler_graph.graph[item]) for item in euler_graph.graph) + "\n" + 30*"="


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
        v = g.graph.get(n1, list())
        v.append(n2)
        g.graph[n1] = v

    return g

def euler_path(euler_graph):
    """ Find the path in given Euler graph. """
    
    # Init stack of visited nodes and reconstructed sequence.
    stack = []
    path = []
    
    # Find the first node to start with.
    node = euler_graph.find_beginning()
    print("Starting node: %s" % node)
    
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
    
    # Create graph.
    euler_graph = get_graph("TAATGCCATGGGATGTT", 3)
    print(euler_graph)
    
    # Find sequence (Euler path) in the graph.
    sequence = euler_path(euler_graph)
    print("Found sequence:   %s" % sequence)
    print("Desired sequence: TAATGCCATGGGATGTT" )