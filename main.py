from classes.Node import Node
from classes.Network import Network

from classes.components.Resistance import Resistance
from classes.components.Source import Source

# Create nodes
node1 = Node()
node2 = Node()

resistance = Resistance(5)
source = Source(5)

# Connect nodes
node1.connect_to(resistance, "in")
node1.connect_to(source, "out")

node2.connect_to(resistance, "out")
node2.connect_to(source, "in")

network = Network()
network.add_node(node1)
network.add_node(node2)
network.add_component(source)
network.add_component(resistance)
network.solve()

# solver = JFNKsolver()

# # nod 2
# solver.add_equation(2, ["source_current", "resistance_current"], lambda x: x[1] - x[0])
# # source
# solver.add_equation(1, ["node2_potential"], lambda x : x[0] - source.Vs)
# # resistance
# solver.add_equation(2, ["node2_potential", "resistance_current"], lambda x : (x[0])/resistance.R - x[1])

# solver.solve(ndigits=2)
