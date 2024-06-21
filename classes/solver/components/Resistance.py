class Resistance:
    def __init__(self, R):
        self.R = R

        self.current = 0
        self.sockets = {"in": None, "out": None}

    def get_type(self):
        return self.type

    def get_sockets(self):
        return self.sockets

    def set_current(self, current):
        self.current = current

    def get_current(self):
        return self.current

    # u_in, u_out, i
    def function(self):
        return lambda x: (x[0] - x[1]) / self.R - x[2]
