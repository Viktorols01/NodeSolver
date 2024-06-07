class ImpedanceConnection:
    def __init__(self, Z):
            self.Z = Z

    def function(self, u_from, u_to):
            return (u_from - u_to)/self.Z

    def derivative(self, u_from, u_to):
            return 1/self.Z