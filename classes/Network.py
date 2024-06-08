from classes.JFNKsolver import JFNKsolver

class Network:
    def __init__(self, complex = False):
        self.complex = complex

        self.nodes = []
        self.node_names = []
        self.node_count = 0
        self.components = []
        self.component_names = []
        self.component_count = 0

    def add_node(self, node):
        self.nodes.append(node)
        self.node_names.append(f"node {self.node_count}")
        self.node_count += 1

    def add_component(self, component):
        self.components.append(component)
        self.component_names.append(f"component {self.component_count}")
        self.component_count += 1

    def solve(self, initial_value = 1, ndigits = 2):
        if self.complex:
            solver = JFNKsolver(initial_value=initial_value, dtype=complex)
        else:
            solver = JFNKsolver(initial_value=initial_value, dtype=float)
        self.add_node_equations(solver)
        self.add_component_equations(solver)
        solver.solve(verbose=True, ndigits=ndigits)
        
        variable_map = solver.get_variable_map()
        for variable_name in variable_map:
            variable_value = variable_map[variable_name]

            type = variable_name.split(" ")[0]
            if type == "node":
                index = self.node_names.index(variable_name)
                self.nodes[index].set_potential(variable_value)
            else:
                index = self.component_names.index(variable_name)
                self.components[index].set_current(variable_value)

    def add_node_equations(self, solver):
        solver.add_equation(1, [self.node_names[0]], lambda x: x[0])

        for i in range(1, self.node_count):
            node = self.nodes[i]
            connections = node.get_connections()
            n = len(connections)
            sign_list = []
            name_list = []
            for pair in connections:
                component, socket = pair
                if socket == "in":
                    sign_list.append(-1)
                elif socket == "out":
                    sign_list.append(1)
                else:
                    raise Exception("socket is not 'in' or 'our'")
                
                index = self.components.index(component)
                name_list.append(self.component_names[index])

            # viktigt: early binding!
            def function(x, sign_list_, n_):
                sum = 0
                for j in range(n_):
                    sum += sign_list_[j]*x[j]
                return sum
            solver.add_equation(n, name_list, lambda x, s = sign_list, t = n: function(x, s, t))

    def add_component_equations(self, solver):
        for i in range(self.component_count):
            component = self.components[i]
            name = self.component_names[i]

            node_in = component.get_sockets()["in"]
            index_in = self.nodes.index(node_in)
            name_in = self.node_names[index_in]

            node_out = component.get_sockets()["out"]
            index_out = self.nodes.index(node_out)
            name_out = self.node_names[index_out]

            solver.add_equation(3, [name_in, name_out, name], component.function())