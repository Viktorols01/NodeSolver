from classes.nodes.Node import Node
from classes.solvers.Network import Network_solver

from classes.components.Impedance import Impedance
from classes.components.Source import Source
from classes.components.Diode import Diode

# Create nodes
node1 = Node()
node2 = Node()
node3 = Node()

# Create components
resistance1 = Impedance(2)
diode = Diode(0.01)
source = Source(10)

# Connect nodes
node1.connect_to(resistance1, "out")
node1.connect_to(source, "in")

node2.connect_to(source, "out")
node2.connect_to(diode, "in")

node3.connect_to(diode, "out")
node3.connect_to(resistance1, "in")

# Add to network and solve
network = Network_solver()
network.add_node(node1)
network.add_node(node2)
network.add_node(node3)
network.add_component(resistance1)
network.add_component(source)
network.add_component(diode)
network.solve(initial_value=1, ndigits=2)

# Solved results:
print("Node 1", node1.get_potential(), "V")
print("Node 2", node2.get_potential(), "V")
print("Node 3", node3.get_potential(), "V")
print("Resistance 1", resistance1.get_current(), "A")
print("Source", source.get_current(), "A")
print("Diode", diode.get_current(), "A")