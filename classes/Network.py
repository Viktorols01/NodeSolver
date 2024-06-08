from classes.JFNKsolver import JFNKsolver

class Network:
    def __init__(self):
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

    def solve(self):
        solver = JFNKsolver(initial_value=0)
        self.add_node_equations(solver)
        self.add_component_equations(solver)
        solver.solve(verbose=True, ndigits=2)
        
        variable_map = solver.get_variable_map()
        print(variable_map)
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
            def function(x):
                sum = 0
                for i in range(n):
                    sum += sign_list[i]*x[i]
                return sum
            solver.add_equation(n, name_list, function)

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

            if index_in == 0:
                solver.add_equation(3, [name_out, name_in, name], component.function_in_known())
            elif index_out == 0:
                solver.add_equation(3, [name_out, name_in, name], component.function_out_known())
            else:
                solver.add_equation(3, [name_out, name_in, name], component.function())
            