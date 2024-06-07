from classes.Node import Node
from classes.Network import Network
from classes.ImpedanceConnection import ImpedanceConnection

# Create nodes
node1 = Node("1")
node1.setCurrent(2.5)

node2 = Node("2")
node2.setPotential(-5)


# Connect nodes
node1.connect(ImpedanceConnection(1), node2)

# Create network
network = Network()
network.add(node1)
network.add(node2)

# Print unsolved network
print("nUnsolved:")
network.print(ndigits = 2)

# Solve
network.solve(verbose = False,rtol = 0, atol = 10**-3)

# Print solved network
print("\nSolved:")
network.print(ndigits = 2)