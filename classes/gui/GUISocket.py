# transform takes x, y and returns sx, sy
# connection is the connected connection

class GUISocket:
    def __init__(self, component, positionfunction, max_connections):
        self.component = component
        self.positionfunction = positionfunction
        self.max_connections = max_connections

        self.sockets = []

        self.r = 5

    def add_connection(self, socket):
        if not self.can_connect():
            raise Exception("Max connections exceeded!")
        self.sockets.append(socket)

    def can_connect(self):
        return len(self.sockets) < self.max_connections