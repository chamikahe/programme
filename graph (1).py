class Graph:
    def __init__(self, undirected=True):
        self.undirected = undirected
        self.root = None
        self.vertices = dict()

    def add_vertex(self, value):
        self.vertices[value] = []

    def remove_vertex(self, value):
        if value not in self.vertices:
            raise ValueError('There is no such vertex as ' + str(value))

        del self.vertices[value]

        for vertex, connections in self.vertices.items():
            connections.remove(value)

    def add_edge(self, v1_value, v2_value):
        if v1_value not in self.vertices:
            raise ValueError('There is no such vertex as ' + str(v1_value))
        if v2_value not in self.vertices:
            raise ValueError('There is no such vertex as ' + str(v2_value))
        if v1_value in self.vertices[v2_value]:
            raise ValueError('A connection already exists between ' + str(v1_value) + ' and ' + str(v2_value))

        self.vertices[v1_value].append(v2_value)

        if self.undirected:
            self.vertices[v2_value].append(v1_value)

    def find_a_path(self, start_vertex, end_vertex, path=None):
        if path is None:
            path = []

        if start_vertex not in self.vertices:
            return None

        path.append(start_vertex)

        if start_vertex == end_vertex:
            return path

        for destination_node in self.vertices[start_vertex]:
            if destination_node not in path:
                temp_path = self.find_a_path(destination_node, end_vertex, path)
                if temp_path:
                    return temp_path

        path.remove(start_vertex)
        return None

    def find_path_length(self, start_vertex, end_vertex):
        path = self.find_a_path(start_vertex, end_vertex)
        if path is not None:
            return len(path) - 1
        else:
            return None

    def print_graph(self):
        for vertex, connections in self.vertices.items():
            print(str(vertex) + "  " + str(connections))


'''
g = Graph()

g.add_vertex(5)
g.add_vertex(7)
g.add_vertex(13)
g.add_edge(5, 7)
g.add_edge(13, 5)

g.add_vertex(4)
g.add_vertex(19)
g.add_vertex(11)
g.add_vertex(1)
g.add_edge(4, 13)
g.add_edge(19, 13)
g.add_edge(11, 13)
g.add_edge(1, 5)
g.add_edge(19, 5)
g.add_edge(11, 5)
g.add_edge(4, 11)
g.add_edge(4, 5)
g.add_edge(1, 13)
g.add_edge(19, 4)

# g.add_edge(6, 5)      # Trying to add an edge to a node that doesn't exist
# g.add_edge(19, 4)      # Trying to add a connection that already exists

g.print_graph()

print("---------------------------------------------------------------------------------------------")
g.remove_vertex(5)
g.print_graph()

print("---------------------------------------------------------------------------------------------")
g.print_graph()

print("---------------------------------------------------------------------------------------------")
print(g.find_path(1, 4))
print(g.find_path_length(1, 4))
# print(g.find_path(1, 12))     # Trying to find  apath that doesn't exist
'''

print("Question 1 ###################################################################################")
g = Graph()

g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_edge(1, 2)
g.add_edge(1, 6)
g.add_edge(2, 6)
g.add_edge(5, 6)
g.add_edge(3, 6)
g.add_edge(4, 6)

g.print_graph()
print("---------------------------------------------------------------------------------------------")
print(g.find_a_path(1, 4))
print(g.find_path_length(1, 4))

print("Question 2 ###################################################################################")

dg = Graph(undirected=False)

dg.add_vertex(1)
dg.add_vertex(2)
dg.add_vertex(3)
dg.add_vertex(4)
dg.add_vertex(5)

dg.add_edge(5, 1)
dg.add_edge(1, 2)
dg.add_edge(5, 2)
dg.add_edge(4, 5)
dg.add_edge(4, 2)
dg.add_edge(3, 2)
dg.add_edge(3, 4)

dg.print_graph()
print("---------------------------------------------------------------------------------------------")
print(dg.find_a_path(3, 1))
print(dg.find_path_length(3, 1))