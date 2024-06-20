# transform takes x, y and returns sx, sy
# connection is the connected connection

class GUISocket:
    def __init__(self, positionfunction, max_connections):
        self.positionfunction = positionfunction
        self.connections = []
        self.max_connections = max_connections
        self.r = 5

    def add_connection(self, socket):
        if not self.can_connect(self):
            raise Exception("Max connections exceeded!")
        self.connections.add(socket)
        socket.connections.add(self)

    def can_connect(self):
        return len(self.connections) < self.max_connections