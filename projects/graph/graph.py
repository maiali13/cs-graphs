"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() # set edges of this vert

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)  # set v2 as a neighbor of v1
        else: 
            raise IndexError("Cannot add an edge to a vertex that does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        breadth-first traversal
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # instantaite empty queue and enqueue the starting node
        q = Queue()
        q.enqueue(starting_vertex)

        # create set to store visited vertices
        visited = set()

        while q.size() > 0: # while queue not empty
            # dequeue first vertex
            v = q.dequeue()
            
            # if it hasn't been visited
            if v not in visited:
                # visit it <3 and add to visited set
                visited.add(v)
                # print(f"BFT Visited {v}")
                print(v)

                # add all neighbors to end of the queue
                for edge in self.get_neighbors(v):
                    q.enqueue(edge)

    def dft(self, starting_vertex):
        """
        depth-first traversal with a stack
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # instantaite empty stack and push the starting node
        s = Stack()
        s.push(starting_vertex)

        # create a set to store the visited nodes
        visited = set()

        # while stack not empty
        while s.size() > 0:
            # pop the first item
            v = s.pop()
            # if it's not been visited:
            if v not in visited:
                # visit it <3 and add to visited set
                visited.add(v)
                # print(f"DFT Visited {v}")
                print(v)

                # add all neighbors to end of the stack
                for edge in self.get_neighbors(v):
                    s.push(edge)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        depth-first traversal with recusion
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create set
        if visited is None:
            visited = set()
        
        # visit and add vertex to visited set
        # print(f"DFT Recusive Visted: {starting_vertex}")
        print(starting_vertex)
        visited.add(starting_vertex)

        # recusively visit and add to set for all neighbors
        for edge in self.vertices[starting_vertex]:
            if edge not in visited:
                self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        breadth-first search
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # instantiate empty queue and enqueue path to the starting node
        q = Queue()
        q.enqueue([starting_vertex])

        # create set to store visited vertices
        visited = set()

        while q.size() > 0:
            path = q.dequeue() # dequeue first path

            # grab last item from end of path
            v = path[-1]
            
            # if that vertex hasn't been visited
            if v not in visited:
                # visit it <3 and mark as visited
                visited.add(v)
                
                # check if vertex is the target
                if v == destination_vertex:
                    # if so, return path
                    return path
                
                # add a path to neighbors queue
                for edge in self.get_neighbors(v):
                    new_path = list(path) # copy path
                    new_path.append(edge) # append the neighbor to the end
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        deapth-first search
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # instantiate empty stack and push the starting node
        s = Stack()
        s.push([starting_vertex])

        # create a set to store the visited nodes
        visited = set()

        while s.size() > 0:
            # pop first vertex in path
            path = s.pop()
            
            # grab last item from end of path
            v = path[-1]

            # if that vertex hasn't been visited
            if v not in visited:
                # visit it and mark as visited
                visited.add(v)

                # check if vertex is the target
                if v == destination_vertex:
                    # if so, return path
                    return path
                
                # add path to neighbors stack
                for edge in self.get_neighbors(v):
                    new_path = list(path) # copy path
                    new_path.append(edge) # append the neighbor to the end
                    s.push(new_path)          

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        deapth-first search with recursion
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create new set
        if visited is None:
            visited = set()

        # create new path
        if path is None:
            path = []

        # keeping track of visited vertices
        visited.add(starting_vertex)
        path = path + [starting_vertex]

        # check if vertex is the target
        if starting_vertex == destination_vertex:
            # if so, return path
            return path

        # if not, iterate recurively thru remaining vertices
        for edge in self.vertices[starting_vertex]:
            if edge not in visited:
                new_path = self.dfs_recursive(edge, destination_vertex, visited, path)

                # if new path exists
                if new_path:
                    return new_path
        
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
