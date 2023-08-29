import math


class Node:
    def __init__(self, nodeid, x, y, location_type):
        self.id = nodeid
        self.x = x
        self.y = y
        self.location_type = location_type
        self.edges = []  # Nodes that this node points to

    def add_edge(self, node):
        self.edges.append(node)

    def distance_to(self, node):
        return math.sqrt((node.x - self.x)**2 + (node.y - self.y)**2)

    def __repr__(self):
        return f" {self.id}: ({self.x}, {self.y}, {self.location_type})"

class Water:
    def __init__(self):
        self.nodes = {}

    def add_node(self, idnode, x, y, location_type):
        node = Node(idnode, x, y, location_type)
        self.nodes[idnode] = node
        return node

    def connect_nodes(self, id1, id2):
        if id1 in self.nodes and id2 in self.nodes:
            self.nodes[id1].add_edge(self.nodes[id2])

    def get_distance(self, id1, id2):
        if id1 in self.nodes and id2 in self.nodes:
            return self.nodes[id1].distance_to(self.nodes[id2])
        else:
            return None

    def dfs(self, start_id, visited=None):
        if visited is None:
            visited = set()

        if start_id not in visited:
            visited.add(start_id)
            print(self.nodes[start_id])

            for edge in self.nodes[start_id].edges:
                self.dfs(edge.id, visited)

        return visited

    def edge_list(self):
        for nodeid,node in self.nodes.items():
            print(f"ID: {nodeid} -> ", end="")
            for edge in node.edges:
                print(f"{edge.id} ", end="")
            print()

# Example usage:

river = Water()
n1 = river.add_node(1, 70, 100, 'headwater')
n42 = river.add_node(42, 100, 130, 'junction')
n3 = river.add_node(3, 120, 265, 'headwater')
n4 = river.add_node(4, 120, 285, 'headwater')
n33 = river.add_node(33, 145, 185, 'junction')

n34 = river.add_node(34, 170, 210, 'junction')
n5 = river.add_node(5, 195, 320, 'headwater')
n59 = river.add_node(59, 190, 205, 'junction')


n35 = river.add_node(35, 220, 185, 'junction')
n17 = river.add_node(17, 225, 290, 'headwater')

n18 = river.add_node(17, 240, 140, 'headwater')
n2 = river.add_node(2, 130, 290, 'junction')

river.connect_nodes(1, 42)
river.connect_nodes(42, 33)
river.connect_nodes(42, 3)
river.connect_nodes(3,4)
river.connect_nodes(4,33)
river.connect_nodes(33,34)
river.connect_nodes(34,5)
river.connect_nodes(34,59)
river.connect_nodes(59,35)
river.connect_nodes(59,17)
river.connect_nodes(35,18)
river.connect_nodes(35,2)


print("Distance between Node 1 and Node 2:", river.get_distance(1, 2))
print("DFS Traversal:")
river.dfs(1)

print(river.edge_list())
