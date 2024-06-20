from classes.gui.GUIComponent import GUIComponent
from classes.gui.GUISocket import GUISocket


class GUINode(GUIComponent):
    def __init__(self, x, y):
        self.socket = GUISocket(self, lambda: (self.x + self.w / 2, self.y + self.h/2), 7)
        super().__init__(x, y, self.socket.r, self.socket.r, [self.socket])

    def render(self, canvas):
        self.render_sockets(canvas)