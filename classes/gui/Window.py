import tkinter as tk

from classes.gui.GUINode import GUINode
from classes.gui.GUIResistance import GUIResistance
from classes.gui.GUISource import GUISource


class Window:
    def __init__(self, width, height, solve):
        self.root = tk.Tk()
        self.root.title("NodeSolver")

        self.is_creating_connection = False
        self.connecting_socket = None
        self.current_x = 0
        self.current_y = 0
        self.held_x = 0
        self.held_y = 0
        self.held_offset_x = 0
        self.held_offset_y = 0

        self.components = []
        resistance_button = tk.Button(self.root, text="Resistance", command=lambda : self.components.append(GUIResistance(20, 20)))
        resistance_button.pack()
        source_button = tk.Button(self.root, text="Source", command=lambda : self.components.append(GUISource(20, 20)))
        source_button.pack()

        source_button = tk.Button(self.root, text="Solve", command=lambda : solve(self))
        source_button.pack()

        self.canvas = tk.Canvas(self.root, background="red", width=width, height=height)
        self.canvas.pack()

        self.canvas.bind("<Motion>", self.__motion)
        self.canvas.bind("<Button-1>", self.__clicked_left)
        self.canvas.bind("<B1-Motion>", self.__moved_left)
        self.canvas.bind("<ButtonRelease-1>", self.__released_left)
        self.canvas.bind("<Button-3>", self.__clicked_right)
        self.canvas.bind("<B3-Motion>", self.__moved_right)
        self.canvas.bind("<ButtonRelease-3>", self.__released_right)

        self.root.after(10, self.render)
        self.root.mainloop()

    def __motion(self, event):
        pass
    
    def __clicked_left(self, event):
        self.current_x = event.x
        self.current_y = event.y
        self.held_x = event.x
        self.held_y = event.y

        for component in self.components:
            touch_socket, socket = component.touched_socket(event.x, event.y)
            if touch_socket:
                if socket.can_connect():
                    self.is_creating_connection = True
                    self.connecting_socket = socket
                    return

    def __moved_left(self, event):
        self.current_x = event.x
        self.current_y = event.y

    def __released_left(self, event):
        def connect(node1, node2):
            node1.add_connection(node2)
            node2.add_connection(node1)

        if self.is_creating_connection:
            self.is_creating_connection = False
            at_reasonable_distance = (self.current_x - self.held_x)**2 + (self.current_y - self.held_y)**2 > 100
            if at_reasonable_distance:
                for component in self.components:
                    touch_socket, socket = component.touched_socket(event.x, event.y)
                    if touch_socket:
                        connect(self.connecting_socket, socket)
                        return
                node = GUINode(self.current_x, self.current_y)
                connect(self.connecting_socket, node.socket)
                self.components.append(node)
                return

    def __clicked_right(self, event):
        self.current_x = event.x
        self.current_y = event.y
        self.held_x = event.x
        self.held_y = event.y

        for component in self.components:
            if component.touched(event.x, event.y):
                self.held_offset_x = event.x - component.x
                self.held_offset_y = event.y - component.y
                component.is_dragged = True
                return

    def __moved_right(self, event):
        self.current_x = event.x
        self.current_y = event.y

        for component in self.components:
            if component.is_dragged:
                component.move(event.x - self.held_offset_x, event.y - self.held_offset_y)
                return

    def __released_right(self, event):
        for component in self.components:
            if component.is_dragged:
                component.is_dragged = False

    def render(self):
        self.canvas.delete("all")
        for component in self.components:
            component.render(self.canvas)

        if self.is_creating_connection:
            self.canvas.create_line(
                self.held_x,
                self.held_y,
                self.current_x,
                self.current_y,
                dash = (2, 2)
            )

        self.canvas.pack()
        self.root.after(10, self.render)
