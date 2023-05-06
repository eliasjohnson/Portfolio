import math

class Graph:
    """graph class
    """
    def __init__(self):
        '''Initialize the graph'''

        self.vertices = {}
        self.edges = {}
        self.weights = {}

    def add_vertex(self,label):
        '''add a vertex with the specified label. return the graph.
        label must be a string or raise ValueError'''

        if not isinstance(label, str):
            raise ValueError("Label must be a string")
        self.vertices[label] = []
        self.edges[label] = []
        return self


    def add_edge(self,src, dest,w):
        '''add an edge from vertex src to vertex dest with weight w.
        Return the graph. validate src, dest, and w: raise ValueError
        if not valid.'''

        if src not in self.vertices:
            raise ValueError("Vertex %s not in graph" % src)
        if dest not in self.vertices:
            raise ValueError("Vertex %s not in graph" % dest)
        if not isinstance(w, (int, float)):
            raise ValueError("Weight must be a number")
        self.edges[src].append(dest)
        self.weights[(src, dest)] = w

    def get_weight(self,src,dest):
        '''return the weight on edge src-dest or math.inf if no path exists,
        raise Valueerror if src or dest are not in the graph'''

        if src not in self.vertices:
            raise ValueError("Vertex %s not in graph" % src)
        if dest not in self.vertices:
            raise ValueError("Vertex %s not in graph" % dest)
        return self.weights.get((src, dest), math.inf)

    def dfs(self,starting_vertex):
        '''Return a generator for traversing the graph in depth-first order
        starting from the specified vertex. Raise a ValueError if the vertex does not exist.'''

        if starting_vertex not in self.vertices:
            raise ValueError("Vertex %s not in graph" % starting_vertex)
        visited = set()
        stack = [starting_vertex]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(set(self.edges[vertex]) - visited)
                yield vertex

    def bfs(self,starting_vertex):
        """return a generator for traversing the grph in depth first
        order starting from the specified vertex. Raise a ValueError
        if the vertex does not exist"""

        if starting_vertex not in self.vertices:
            raise ValueError("Vertex %s not in graph" % starting_vertex)
        visited = set()
        queue = [starting_vertex]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(set(self.vertices[vertex]) - visited)
                yield vertex

    def dsp(self,src,dest):
        '''Return a tuple (path length , the list of vertices on the path
        from dest back to src). If no path exists, return the tuple
        (math.inf,  empty list.)'''

        if src not in self.vertices:
            raise ValueError("Vertex %s not in graph" % src)
        if dest not in self.vertices:
            raise ValueError("Vertex %s not in graph" % dest)
        if src == dest:
            return (0, [src])
        visited = set()
        queue = [(src, [src])]
        while queue:
            (vertex, path) = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                for next in set(self.vertices[vertex]) - visited:
                    if next == dest:
                        return (len(path), path + [next])
                    queue.append((next, path + [next]))
        return (math.inf, [])

    def dsp_all(self,src):
        '''Return a dictionary of the shortest weighted path between src
        and all other vertices using Dijkstra's Shortest Path algorithm.
        In the dictionary, the key is the the destination vertex label,
        the value is a list of vertices on the path from src to dest inclusive.'''

        if src not in self.vertices:
            raise ValueError("Vertex %s not in graph" % src)
        visited = set()
        queue = [(src, [src])]
        while queue:
            (vertex, path) = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                for next in set(self.vertices[vertex]) - visited:
                    queue.append((next, path + [next]))
        return visited

    def __str__(self):
        '''Return a string representation of the graph'''
        return "Graph: %s" % self.vertices

def main():
    '''contruct the graph. print it to the console.
    print results of DFS starting with vertex A.
    print results of BFS starting with vertex A.
    print the path from vertex A to vertex F.
    print the shortest paths from vertex A to all other vertices.'''

    graph_ = Graph()
    graph_.add_vertex("A")
    graph_.add_vertex("B")
    graph_.add_vertex("C")
    graph_.add_vertex("D")
    graph_.add_vertex("E")
    graph_.add_vertex("F")

    graph_.add_edge("A", "B", 2.0)
    graph_.add_edge("A", "F", 9.0)
    graph_.add_edge("B", "F", 6.0)
    graph_.add_edge("B", "C", 8.0)
    graph_.add_edge("B", "D", 15.0)
    graph_.add_edge("C", "D", 1.0)
    graph_.add_edge("E", "D", 3.0)
    graph_.add_edge("E", "C", 7.0)
    graph_.add_edge("F", "E", 3.0)

    print(graph_)
    print("DFS: ", end="")
    for vertex in graph_.dfs("A"):
        print(vertex, end=" ")
    print()
    print("BFS: ", end="")
    for vertex in graph_.bfs("A"):
        print(vertex, end=" ")
    print()
    print("DSP: ", end="")
    for vertex in graph_.dsp("A", "F"):
        print(vertex, end=" ")
    print()
    print("DSP_ALL: ", end="")
    for vertex in graph_.dsp_all("A"):
        print(vertex, end=" ")
    print()

if __name__ == "__main__":
    main()
