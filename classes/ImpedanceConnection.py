class ImpedanceConnection:
    def __init__(self, Z):
            self.Z = Z

    # current flowing from u_from to u_to
    def function(self, u_from, u_to):
            return (u_from - u_to)/self.Z

    # derivative with respect to u_from
    def derivative(self, u_from, u_to):
            return 1/self.Z