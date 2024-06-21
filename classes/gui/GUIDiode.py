from classes.gui.abstract.GUIDraggable import GUIDraggable
from classes.gui.sub.GUISocket import GUISocket
from classes.solver.components.Diode import Diode
from classes.solver.components.Resistance import Resistance


class GUIDiode(GUIDraggable):
    def __init__(self, x, y):
        self.math_component = Diode()

        socket1 = GUISocket(self, lambda: (self.x, self.y + self.h / 2), 1)
        socket2 = GUISocket(self, lambda: (self.x + self.w, self.y + self.h / 2), 1)
        super().__init__(x, y, 80, 80, [socket1, socket2])

    def render(self, canvas):
        self.render_base(canvas)
        points = [
            self.x,
            self.y,
            self.x + self.w,
            self.y + self.h / 2,
            self.x,
            self.y + self.h,
        ]
        canvas.create_polygon(
            points,
            outline="black",
            fill="white",
            width=2,
        )
        self.render_sockets(canvas, current=self.math_component.get_current())
