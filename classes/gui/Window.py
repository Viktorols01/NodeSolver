import pygame as pg
import tkinter as tk

class Window:
    def __init__(self):
        pg.init()
        screen = pg.display.set_mode((1000, 1000))
        timer = pg.time.Clock()
        loop = True
        while loop:
            screen.fill("white")

            pos = pg.mouse.get_pos()
            for event in pg.event.get():
                print(event)
                if event.type == pg.QUIT:
                    loop = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    type = pop_window(["1", "2", "3"])
                    print(type)

            pg.display.flip()
            timer.tick(60)
        
        pg.quit()

def pop_window(options):
    w = tk.Tk()
    w.title("Select option")

    def handle_button_press(event, option):
        w.destroy()
        return option
    
    for option in options:
        btn = tk.Button(w, text=option, command=lambda e: handle_button_press(e, option))
        btn.pack()
    
    w.mainloop()

