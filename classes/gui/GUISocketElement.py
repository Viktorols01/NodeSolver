class GUISocketElement:
        def __init__(self, sockets):
            self.sockets = sockets

        def render_sockets(self, canvas):
            for socket in self.sockets:
                sx, sy = socket.positionfunction()
                canvas.create_oval(sx - socket.r, sy - socket.r, sx + socket.r, sy + socket.r)
        
        def touched_socket(self, x, y):
            for socket in self.sockets:
                sx, sy = socket.positionfunction()
                dist = ((x - sx)**2 + (y - sy)**2)**(1/2)
                if dist <= socket.r:
                    return (True, (sx, sy))
            return (False, (0, 0))