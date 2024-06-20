from classes.gui.GUISocketElement import GUISocketElement

# alltid rektangulära, men sockets kan vara på olika positioner

class GUIComponent(GUISocketElement):
        def __init__(self, x, y, w, h, sockets):
            super().__init__(sockets)
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.is_dragged = False

        def render(self, canvas):
            canvas.create_rectangle(
                self.x,
                self.y,
                self.x + self.w,
                self.y + self.h,
                outline="black",
                fill="white",
                width=2,
            )
            self.render_sockets(canvas)

        def touched(self, x, y):
            if x > self.x and x < self.x + self.w:
                if y > self.y and y < self.y + self.y:
                    return True
            return False

        def move(self, x, y):
            self.x = x
            self.y = y