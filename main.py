from classes.Node import Node
from classes.Network import Network

from classes.components.Resistance import Resistance
from classes.components.Source import Source
from classes.components.Diode import Diode

# Create nodes
node1 = Node()
node2 = Node()
#node3 = Node()

# Create components
resistance1 = Resistance(2)
resistance2 = Resistance(2)
#diode = Diode(1)
source = Source(5)

# Connect nodes
node1.connect_to(resistance1, "out")
node1.connect_to(resistance2, "out")
node1.connect_to(source, "in")

node2.connect_to(source, "out")
node2.connect_to(resistance1, "in")
node1.connect_to(resistance2, "in")

#node3.connect_to(diode, "out")
#node3.connect_to(resistance1, "in")

# Add to network and solve
network = Network()
network.add_node(node1)
network.add_node(node2)
#network.add_node(node3)
network.add_component(resistance1)
network.add_component(resistance2)
network.add_component(source)
#network.add_component(diode)
network.solve(initial_value=1, ndigits=5)

# Solved results:
print("Node 1", node1.get_potential())
print("Node 2", node2.get_potential())
#print("Node 3", node3.get_potential())
print("Resistance 1", resistance1.get_current())
print("Resistance 2", resistance1.get_current())
print("Source", source.get_current())
#print("Diode", diode.get_current())