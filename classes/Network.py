import numpy as np

class Network:
    def __init__(self):
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)

    def function(self):
        n = len(self.nodes)
        vector = np.zeros(shape = [n], dtype = float)
        for i in range(n):
            node = self.nodes[i]
            vector[i] = node.function()
        return vector

    def solve(self, verbose = False, rtol = 0, atol = 10**-3):
        res_init = np.linalg.norm(self.function())

        k = 1
        while np.linalg.norm(self.function()) > rtol*res_init + atol:
            if verbose:
                print("Iteration",k)
            self.solveIteration(verbose)
            k += 1
        if verbose:
            print("Newton-Raphson finished in",k,"iterations.")
            print("Initial norm:", res_init)
            print("Final norm", np.linalg.norm(self.function()))

    def solveIteration(self, verbose):
        n = len(self.nodes)
        jacobian = np.zeros(shape = [n, n], dtype = float)
        for i in range(n):
            node = self.nodes[i]

            assert(node.current_known != node.potential_known)

            if not node.current_known:
                jacobian[i][i] -= 1 # current in
            else:
                for pair in node.connections:
                    (connection, subnode) = pair
                    j = self.nodes.index(subnode)
                    jacobian[j][i] -= connection.derivative(node.potential, subnode.potential) # current in for subnode
                    if not node.potential_known:
                        jacobian[i][i] += connection.derivative(node.potential, subnode.potential) # current out
        function = self.function()

        if verbose:
            print("Jacobian:\n", jacobian)
            print("Function:", function)

        df = np.linalg.solve(jacobian, -self.function())
        if verbose:
            print("df", df)

        for i in range(n):
            node = self.nodes[i]
            if not node.current_known:
                node.current += df[i]
            if not node.potential_known:
                node.potential += df[i]

    def print(self, ndigits = 0):
        for node in self.nodes:
            node.print(ndigits = ndigits)