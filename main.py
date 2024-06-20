from classes.gui.GUINode import GUINode
from classes.gui.GUIResistance import GUIResistance
from classes.gui.GUISource import GUISource
from classes.gui.Window import Window
from classes.solver.components.Resistance import Impedance
from classes.solver.components.Source import Source
from classes.solver.nodes.Node import Node

def solve(window):
    # Create nodes and components
    nodes = []
    for component in window.components:
        if isinstance(component, GUINode):
            nodes.append(Node())
        elif isinstance(component, GUIResistance):
            nodes.append(Impedance(5))
        elif isinstance(component, GUISource):
            nodes.append(Source(10))

window = Window(800, 800, lambda window : solve(window))