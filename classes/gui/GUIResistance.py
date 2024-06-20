from classes.gui.GUIComponent import GUIComponent
from classes.gui.GUISocket import GUISocket


class GUIResistance(GUIComponent):
    def __init__(self, x, y):
        socket1 = GUISocket(self, lambda : (self.x, self.y + self.h / 2), 1)
        socket2 = GUISocket(self, lambda : (self.x + self.w, self.y + self.h / 2), 1)
        super().__init__(x, y, 100, 40, [socket1, socket2])

    def render(self, canvas):
        self.render_base(canvas)