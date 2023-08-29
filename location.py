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

#add the node and t

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

n18 = river.add_node(18, 240, 140, 'headwater')
n2 = river.add_node(2, 130, 290, 'junction')
n19 = river.add_node(19, 330, 185, 'headwater')

n36 = river.add_node(36, 275, 250, 'junction')
n20 = river.add_node(20, 330, 200, 'headwater')
n37 = river.add_node(37, 290, 270, 'junction')

n16 = river.add_node(16, 245, 330, 'headwater')
n39 = river.add_node(39, 320, 290, 'junction')
n55 = river.add_node(5, 360, 260, 'junction')
n38 = river.add_node(38, 325, 335, 'junction')


#connect the node
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
river.connect_nodes(35,19)
river.connect_nodes(3,36)
river.connect_nodes(36,20)
river.connect_nodes(36,37)
river.connect_nodes(37,16)
river.connect_nodes(37,39)
river.connect_nodes(39,55)
river.connect_nodes(39,38)


# try to calculate the distance
print("Distance between Node 1 and Node 2:", river.get_distance(1, 2))
print("DFS Traversal:")

# travel the nodes
river.dfs(1)
# a method for travel all nodes
### some expain for dfs(1)
#Suppose  3 nodes connected as `1 -> 2 -> 3`.
#1. `dfs(1)`.
#2. Node 1 is not in the `visited` set. Add it, print its details.
#3. Check Node 1's edges. We find Node 2. do`dfs(2)`.
#4. Node 2 is not in the `visited` set. Add it, print its details.
#5. Check Node 2's edges. We find Node 3. do `dfs(3)`.
#6. Node 3 is not in the `visited` set. Add it, print its details.
#7. Node 3 has no unvisited edgess. Return from `dfs(3)`.
#8. Return from `dfs(2)`.
#9. Return from `dfs(1)`.
#The output will display the details of the nodes in the order they were visited: Node 1, Node 2, and then Node 3.

# check the edge
print(river.edge_list())