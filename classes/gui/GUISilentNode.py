from classes.gui.Help import interpolate
from classes.gui.sub.GUISocket import GUISocket
from classes.gui.abstract.GUIDraggable import GUIDraggable
from classes.solver.components.Source import Source


class GUISilentNode(GUIDraggable):
    def __init__(self, socket_in_outer, socket_out_outer):
        self.math_component = Source(0)

        self.socket_in_outer = socket_in_outer
        self.socket_out_outer = socket_out_outer

        socket1 = GUISocket(
            self,
            lambda: interpolate(
                self.socket_in_outer.positionfunction(),
                self.socket_out_outer.positionfunction(),
                1 / 2,
            ),
            1,
        )
        socket2 = GUISocket(
            self,
            lambda: interpolate(
                self.socket_in_outer.positionfunction(),
                self.socket_out_outer.positionfunction(),
                1 / 2,
            ),
            1,
        )
        super().__init__(0, 0, 0, 0, [socket1, socket2])

    def render(self, canvas):
        # (x, y) = interpolate(
        #     self.socket_in_outer.positionfunction(),
        #     self.socket_out_outer.positionfunction(),
        #     1 / 2,
        # )
        # canvas.create_oval(x - 20, y - 20, x + 20, y + 20)
        self.render_sockets(canvas, current=self.math_component.get_current())
