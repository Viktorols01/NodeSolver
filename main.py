from classes.Node import Node
from classes.Network import Network
from classes.ImpedanceConnection import ImpedanceConnection

# Create nodes
node1 = Node("1")
node1.setPotential(5)

node2 = Node("2")
node2.setCurrent(2)

node3 = Node("3")
node3.setPotential(0)


# Connect nodes
node1.connect(ImpedanceConnection(1), node2)
node1.connect(ImpedanceConnection(1), node3)
node2.connect(ImpedanceConnection(2), node3)

# Create network
network = Network()
network.add(node1)
network.add(node2)
network.add(node3)

# Print unsolved network
print("nUnsolved:")
network.print(ndigits = 2)

# Solve
network.solve(verbose = True,rtol = 0, atol = 10**-3)

# Print solved network
print("\nSolved:")
network.print(ndigits = 2)