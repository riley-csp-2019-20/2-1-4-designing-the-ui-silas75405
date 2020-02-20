import tkinter as tk
root = tk.Tk()
root.wm_geometry("200x200")

root.grid()

blue = tk.Canvas(width = 125, height = 100, background = "blue")
blue.grid(row = 0, column = 0)

red = tk.Canvas(width = 125, height = 100, background = "red")
red.grid(row = 1, column = 0)

green = tk.Canvas(width = 75, height = 100, background = "green")
green.grid(row = 0, column = 1)

yellow = tk.Canvas(width = 75, height = 100, background = "yellow")
yellow.grid(row = 1, column = 1)

root.mainloop()