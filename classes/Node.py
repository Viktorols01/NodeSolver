class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []

        self.potential_known = False
        self.current_known = False
        self.potential = 0
        self.current = 0

    def setPotential(self, potential):
        self.potential = potential
        self.potential_known = True

    def setCurrent(self, current):
        self.current = current
        self.current_known = True

    def connect(self, connection, node):
        pair = (connection, node)
        self.connections.append(pair)

        pair_reversed = (connection, self)
        node.connections.append(pair_reversed)

    def function(self):
        sum = 0
        for pair in self.connections:
            (connection, node) = pair
            sum += connection.function(self.potential, node.potential)

        sum -= self.current
        return sum

    # --- DEBUG ---
    def print(self, ndigits = 0):
        print("Node ", self.name)
        if self.potential_known:
            print("\tPotential (set):", round(self.potential, ndigits),"V")
        else:
            print("\tPotential:", round(self.potential, ndigits),"V")
        if self.current_known:
            print("\tCurrent (set):", round(self.current, ndigits), "A")
        else:
            print("\tCurrent:", round(self.current, ndigits), "A")
        #print("\tFunction:", self.function())