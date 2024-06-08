from classes.Node import Node
from classes.Network import Network

from classes.components.Resistance import Resistance
from classes.components.Source import Source

# Create nodes
node1 = Node()
node2 = Node()
node3 = Node()

resistance1 = Resistance(3)
resistance2 = Resistance(5)
resistance3 = Resistance(5)
source = Source(12)

# Connect nodes
node1.connect_to(source, "in")
node1.connect_to(resistance2, "out")
node1.connect_to(resistance3, "out")

node2.connect_to(source, "out")
node2.connect_to(resistance1, "in")

node3.connect_to(resistance1, "out")
node3.connect_to(resistance2, "in")
node3.connect_to(resistance3, "in")


network = Network()
network.add_node(node1)
network.add_node(node2)
network.add_node(node3)
network.add_component(resistance1)
network.add_component(resistance2)
network.add_component(resistance3)
network.add_component(source)
network.solve()

# Solved results:
print("Node 1", node1.get_potential())
print("Node 2", node2.get_potential())
print("Node 3", node3.get_potential())

print("Resistance 1", resistance1.get_current())
print("Resistance 2", resistance2.get_current())
print("Resistance 3", resistance3.get_current())

print("Source", source.get_current())