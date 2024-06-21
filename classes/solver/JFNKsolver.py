import numpy as np
import scipy

from classes.solver.Equation import Equation


class JFNKsolver:

    def __init__(self, initial_value=1, dtype=float):
        self.initial_value = initial_value
        self.dtype = dtype

        # Equations in system
        self.equations = []

        # String to variable value, map
        self.variable_values_map = {}

        # Index to variable value, vector
        self.variable_values = None
        self.variable_names = None
        self.name_to_index = None

    def add_equation(
        self, variable_count, variable_names, function, variable_values=None
    ):
        assert variable_count == len(
            variable_names
        ), "variable_count not equal to length of variable_names"

        if not variable_values is None:
            assert variable_count == len(
                variable_values
            ), "variable_count not equal to length of variable_values"

        for i in range(variable_count):
            name = variable_names[i]
            if variable_values is None:
                value = self.initial_value
            else:
                value = variable_values[i]
            if not name in self.variable_values_map:
                self.variable_values_map[name] = value

        self.equations.append(Equation(variable_count, variable_names, function))

    def solve(self, verbose=False, rtol=0, atol=10**-3, ndigits=10):
        self.__vectorize()

        res_init = np.linalg.norm(self.__get_function(self.__get_vector()))
        res = res_init

        du = 0

        k = 0
        while res > rtol * res_init + atol:
            k += 1
            if verbose:
                print("Iteration", k)
                print("Function", self.__get_function(self.__get_vector()))
                print("Residual", res)
                print("Variables:")
                for i in range(len(self.variable_values)):
                    name = self.variable_names[i]
                    value = self.variable_values[i]
                    print(name, value)
                print("Previous variable increment", du)

            du = self.__solveIteration(verbose=verbose)
            self.variable_values = self.variable_values + du

            res = np.linalg.norm(self.__get_function(self.__get_vector()))

        if verbose:
            print("Newton-Raphson finished in", k, "iterations.")
            print("Initial norm:", res_init)
            print(
                "Final norm", np.linalg.norm(self.__get_function(self.__get_vector()))
            )

        self.__devectorize(ndigits)

    def get_variable_map(self):
        return self.variable_values_map

    # Must be called after adding all equations?
    def __vectorize(self):
        n = len(self.equations)
        self.variable_values = np.zeros(shape=[n], dtype=self.dtype)
        self.variable_names = []
        self.name_to_index = {}

        assert n <= len(
            self.variable_values_map
        ), f"more equations ({n}) than variables ({len(self.variable_values_map)})"
        assert n >= len(
            self.variable_values_map
        ), f"more variables ({len(self.variable_values_map)}) than equations ({n})"

        i = 0
        for name in self.variable_values_map:
            value = self.variable_values_map[name]
            self.variable_values[i] = value
            self.variable_names.append(name)
            self.name_to_index[name] = i
            i += 1

    def __devectorize(self, ndigits=10):
        n = len(self.variable_values)
        for i in range(n):
            name = self.variable_names[i]
            self.variable_values_map[name] = round(self.variable_values[i], ndigits)

    def __get_vector(self):
        return self.variable_values

    # return function with values q
    def __get_function(self, u):
        n = len(self.equations)
        vector = np.zeros(shape=[n], dtype=self.dtype)
        for i in range(n):
            equation = self.equations[i]
            variable_values = []
            for j in range(equation.variable_count):
                name = equation.variable_names[j]
                index = self.name_to_index[name]
                variable_values.append(u[index])
            vector[i] = equation.evaluate(variable_values)
        return vector

    def __get_jacobian_product(self, q):
        if np.linalg.norm(q) == 0:
            epsilon = 10**-7
        else:
            epsilon = 10**-7 / np.sqrt(np.linalg.norm(q))

        u0 = self.__get_vector()
        product = (
            self.__get_function(u0 + q * epsilon) - self.__get_function(u0)
        ) / epsilon
        return product

    def __solveIteration(self, verbose=False):
        n = len(self.variable_values)

        A = scipy.sparse.linalg.LinearOperator(
            (n, n), matvec=self.__get_jacobian_product
        )
        du, info = scipy.sparse.linalg.gmres(
            A, -self.__get_function(self.__get_vector())
        )

        return du
