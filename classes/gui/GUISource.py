from classes.gui.GUIComponent import GUIComponent
from classes.gui.GUISocket import GUISocket


class GUISource(GUIComponent):
    def __init__(self, x, y):
        socket1 = GUISocket(self, lambda: (self.x, self.y + self.h / 2), 1)
        socket2 = GUISocket(self, lambda: (self.x + self.w, self.y + self.h / 2), 1)
        super().__init__(x, y, 20, 100, [socket1, socket2])

    def render(self, canvas):
        self.render_base(canvas)
        canvas.create_text((self.x + self.w / 2, self.y + 10), text="+")
        canvas.create_text((self.x + self.w / 2, self.y + self.h - 10), text="-")
