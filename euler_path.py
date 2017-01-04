from collections import defaultdict

class Graph:
    """
    Graph represented as a dict.
    Keys: kmers (string).
    Values: List of neighbouring kmers (string).
    """
    
    def __init__(self):
        """
        Construct a sensible empty graph. self.indeg is technically not needed, but is a useful syntactic sugar.
        """
        self.graph = defaultdict(list)
        self.indeg = defaultdict(lambda: 0)
        self.outdeg = defaultdict(lambda: 0)

    def add_arrow(self, src, dest):
        """
        Adds an arrow from node src to node dest to the graph.
        """
        self.graph[src].append(dest)
        self.outdeg[src] += 1
        self.indeg[dest] += 1
    
    def find_beginning(self):
        """
        Find the node to begin searching for Euler path with.
        TODO Terrible complexity, would be nice to remember starting node when creating the graph
        and just give it as an argument.
        """
        
        return_node = None
        for node in self.graph:
            return_node = node
            # If out > into, we should begin with that node.
            if self.outdeg[node] > self.indeg[node]:
                return return_node
            
        # All nodes have even degree, the graph is Euler cycle, first node can be whatever node.
        return return_node
    
    def __str__(self):
        return 30*"=" + "\nGraph:\n" + "\n".join(str(item) + " (>%d, %d>)" % (self.indeg[item], self.outdeg[item]) + ": " + " ".join(str(item) for item in euler_graph.graph[item]) for item in euler_graph.graph) + "\n" + 30*"="


def get_kmers(sequence, k, d=1):
        for i in range(0, len(sequence) - (k - 1), d):
            yield sequence[i:i+k]

def get_graph(sequence, k):
    g = Graph()
    kmers = get_kmers(sequence, k)
    for kmer in kmers:
        #we add nodes (k-1 mer) and edge in graph : n1 -> n2
        n1 = kmer[:-1]
        n2 = kmer[1:]
        g.add_arrow(n1, n2)

    return g

def get_paired_kmers(sequence, k, d):
  for i in range(0, len(sequence) - 2 * k - d + 1):
    yield (sequence[i:i+k], sequence[i+k+d:i+2*k+d])
    
def get_paired_graph(sequence, k, d):
  g = Graph()
  pairs = get_paired_kmers(sequence, k, d)
  for pair in pairs:
    n1 = (pair[0][:-1], pair[1][:-1])
    n2 = (pair[0][1:], pair[1][1:])
    g.add_arrow(n1, n2)
    #if n1 not in g:
      #g[n1] = []
    #g[n1].append(n2)
  return g

def euler_path(euler_graph):
    """ Find the path in given Euler graph. """
    
    # Init stack of visited nodes and reconstructed sequence.
    stack = []
    path = []
    
    # Find the first node to start with.
    node = euler_graph.find_beginning()
    print("Starting node: %s" % str(node))
    
    # Go through graph.
    while True:
        if not euler_graph.graph[node]:
            # No more edges going from this node.
            # Append the sequence with the last letter of that node's k-mer.
            path.append(node)
            if not stack:
                # We went through the whole graph.
                #path.append(node)
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
            
    return path

def gapReconstruction(prefixString, suffixString, k, d):
  for i in range(k+d+1,len(prefixString)):
    if prefixString[i] != suffixString[i-k-d]:
      return None
  return prefixString + suffixString[-(k+d):] ##prefixString concatenated with the last k+d symbols of suffixString

def render_path_single(path):
    """
    Generate a reconstructed genome based on the given Eulerian path (reversed) of (k-1)-mer nodes.
    """
    print("path: ", path[::-1])
    return ("".join(map(lambda x: x[-1], path)) + path[-1][-2::-1])[::-1]

def render_path_paired(path, k, d):
    """
    Generate a reconstructed genome based on the given Eulerian path (reversed) of (k, d)-mer nodes.
    TODO this doesn't seem to really work, gapReconstruction above will return None
    """
    path = path[::-1]
    prefix = path[0][0] + "".join(map(lambda x: x[0][-1], path[1:]))
    suffix = path[0][1] + "".join(map(lambda x: x[1][-1], path[1:]))
    return gapReconstruction(prefix, suffix, k, d)

def load_fasta(file_handle):
    string = ""
    line = file_handle.readline()
    if not line or line[0] != ">": return None
    while True:
        line = file_handle.readline()
        if not line or line[0] == ">": break

        line = line.strip()
        if not line or line[0] == ";": continue
        string += line.strip()
    return string

if __name__ == "__main__":
    # Create graph.
    euler_graph = get_graph("TAATGCCATGGGATGTT", 3)
    print(euler_graph)
    
    # Find sequence (Euler path) in the graph.
    sequence = euler_path(euler_graph)
    print("Found sequence:   %s" % render_path_single(sequence))
    print("Desired sequence: TAATGCCATGGGATGTT" )
    
    print("\n\n\nPAIRED GRAPH:")

    # Create graph.
    euler_graph = get_paired_graph("TAATGCCATGGGATGTT", 3, 1)
    print(euler_graph)
    
    # Find sequence (Euler path) in the graph.
    sequence = euler_path(euler_graph)
    print("Found sequence:   %s" % render_path_paired(sequence, 3, 1))
    print("Desired sequence: TAATGCCATGGGATGTT" )
    
    # Try processing an input file.
    from sys import argv, stdin

    if len(argv) < 2 or argv[1] == "-":
        file_handle = stdin
    else:
        file_handle = open(argv[1], "r")
    fasta = load_fasta(file_handle)
    euler_graph = get_graph(fasta, 5)
    print("Found sequence:   %s" % (render_path_single(euler_path(euler_graph))))
    print("Desired sequence: %s" % (fasta))
