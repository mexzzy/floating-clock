import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    root.after(1000, time)

def on_drag(event):
    x, y = event.x_root, event.y_root
    root.geometry(f"+{x - offset_x}+{y - offset_y}")

def on_click(event):
    global offset_x, offset_y
    offset_x, offset_y = event.x, event.y

def toggle_stick():
    global is_sticky
    is_sticky = not is_sticky
    root.attributes('-topmost', is_sticky)
    stick_button.config(text="Sticky: ON" if is_sticky else "Sticky: OFF")

root = tk.Tk()
root.title("Floating Clock")
root.attributes('-topmost', True)

padding_value = 10
border_radius = 10

content_width = 110 + 2 * padding_value

root.overrideredirect(True)
root.tk_setPalette(background='black')

frame = tk.Frame(root, bg='black')
frame.pack()

canvas_frame = tk.Frame(frame, bg='black')
canvas_frame.pack()

canvas = tk.Canvas(canvas_frame, width=content_width, height=40, highlightthickness=0)
canvas.pack()

canvas.create_rectangle(0, 0, content_width, 40, fill='black', outline='black', width=2, tags="rounded")

label = tk.Label(canvas, text="", font=('calibri', 12, 'bold'), bg='black', fg='white', justify='center')
label.place(relx=0.5, rely=0.5, anchor='center')

offset_x, offset_y = 0, 0
canvas.tag_bind("rounded", '<ButtonPress-1>', on_click)
canvas.tag_bind("rounded", '<B1-Motion>', on_drag)

is_sticky = True
stick_button = tk.Button(frame, text="Sticky: ON", command=toggle_stick)
stick_button.pack(side='right')

time()
root.mainloop()
