from classes.components.Component import Component

class Resistance:
    def __init__(self, R):
        self.R = R
        self.type = "Resistance"

        self.current = 0
        self.current = 0
        self.sockets = {"in" : None, "out" : None}

    def get_type(self):
        return self.type

    def get_sockets(self):
        return self.sockets
    
    def set_current(self, current):
        self.current = current

    # u_out, u_in, i
    def function(self):
        return lambda x : (x[0] - x[1])/self.R - x[2]
    
    def function_in_known(self):
        return lambda x : (x[0] - 0)/self.R - x[2]
    
    def function_out_known(self):
        return lambda x : (0 - x[1])/self.R - x[2]