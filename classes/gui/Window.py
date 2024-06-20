import tkinter as tk

from classes.gui.GUIResistance import Resistance


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NodeSolver")

        self.components = []
        self.components.append(Resistance(20, 20))

        self.connections = []

        self.lines = []

        self.canvas = tk.Canvas(self.root, background="red", height=500, width=500)
        self.canvas.pack()
        self.canvas.bind("<Motion>", self.__motion)
        self.canvas.bind("<Button-1>", self.__clicked)
        self.canvas.bind("<B1-Motion>", self.__moved)
        self.canvas.bind("<ButtonRelease-1>", self.__released)
        self.root.after(10, self.render)
        self.root.mainloop()

    def __motion(self, event):
        pass

    def __clicked(self, event):
        for component in self.components:
            touch_socket, socket = component.touched_socket(event.x, event.y)
            if touch_socket:
                print("Creating socket...")
                return

            if component.touched(event.x, event.y):
                print("Dragging component from component...")
                component.is_dragged = True
                return

    def __moved(self, event):
        for component in self.components:
            if component.is_dragged:
                component.move(event.x, event.y)
                return

        for connection in self.connections:
            if connection.is_being_created:
                connection.move(event.x, event.y)

    def __released(self, event):
        for component in self.components:
            if component.is_dragged:
                print("Dropping component...")
                component.is_dragged = False

        for connection in self.connections:
            if connection.is_being_created:
                connection.place(event.x, event.y)

    def render(self):
        self.canvas.delete("all")
        for component in self.components:
            component.render(self.canvas)
        for connection in self.connections:
            connection.render(self.canvas)
        self.canvas.pack()
        self.root.after(10, self.render)
