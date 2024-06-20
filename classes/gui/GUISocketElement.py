class GUISocketElement:
        def __init__(self, sockets):
            self.sockets = sockets

        def render_sockets(self, canvas):
            for socket in self.sockets:
                sx, sy = socket.positionfunction()

                if socket.can_connect():
                    canvas.create_oval(sx - socket.r, sy - socket.r, sx + socket.r, sy + socket.r)

                for socket in socket.sockets:
                     sx2, sy2 = socket.positionfunction()
                     canvas.create_line(sx, sy, sx2, sy2)
        
        def touched_socket(self, x, y):
            for socket in self.sockets:
                sx, sy = socket.positionfunction()
                dist = ((x - sx)**2 + (y - sy)**2)**(1/2)
                if dist <= socket.r:
                    return (True, socket)
            return (False, None)