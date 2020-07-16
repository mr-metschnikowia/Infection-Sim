import tkinter as tk
import time
from random import choice

window = tk.Tk()

spruce = tk.Canvas(window, height = 700, width = 700, bg = '#263D42')
spruce.pack()

frame = tk.Frame(window, bg = 'green')
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

frame_2 = tk.Frame(frame, bg = 'black')
frame_2.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

Canvas_1 = tk.Canvas(frame_2, height = 700, width = 700, bg = 'White')
Canvas_1.pack()

count_red = 0
count_blue = 0
x = -80
y = 360
listo = []
listo_red = []
a = 1
x_2 = 340
y_2 = -80
start_time = time.time()
coords_blue = []
coords_red = []
x_coords = []
y_coords = []
xx = -60
yy = -60
trigger = 1

for i in range(506):
    o3 = Canvas_1.create_oval(90, 90, 100, 100, fill='blue')
    Canvas_1.move(o3, x, y_2)
    listo.append(o3)
    coords_blue.append(Canvas_1.coords(o3))
    x += 20
    count_blue += 1
    if len(listo) % 22 == 0:
        x = -80
        y_2 += 20
        continue

window.update()

input_1 = input('Pathogen Replication Rate (low/medium/high):')

for i in range(21):
    x_coords.append(xx)
    xx += 20

for i in range(22):
    y_coords.append(yy)
    yy += 20

def timer():
    global start_time
    global run_time
    run_time = time.time() - start_time
    return run_time

def create_red():
    global count_red
    o4 = Canvas_1.create_oval(90, 90, 80, 80, fill='red')
    Canvas_1.move(o4, choice(x_coords), choice(y_coords))
    coords_red.append(Canvas_1.coords(o4))
    if Canvas_1.coords(o4) in coords_blue:
        Canvas_1.delete(o4)
    elif count_red > 0 and Canvas_1.coords(o4) == coords_red[len(coords_red) - 2]:
        Canvas_1.delete(o4)
    else:
        listo_red.append(o4)
        count_red += 1

def immune_response():
    global count_red
    global count_blue
    if count_blue > 0:
            gg = choice(range(len(listo_red)))
            Canvas_1.delete(listo_red[gg])
            del(listo_red[gg])
            del(coords_red[gg])
            count_red -= 1

def destroy():
    global count_blue
    if count_blue > 0 and count_red > 7:
        gg = choice(range(len(listo)))
        Canvas_1.delete(listo[gg])
        del(listo[gg])
        del(coords_blue[gg])
        count_blue -= 1

def process_input():
    global input_1
    if input_1 == 'low':
        destroy()
        immune_response()
    elif input_1 == 'high':
        create_red()
        destroy()
    else:
        destroy()

while count_red < 462:
    if count_red < 7:
        create_red()
        Canvas_1.update()
        time.sleep(0.05)
        timer()
    elif run_time < 5:
        create_red()
        destroy()
        Canvas_1.update()
        time.sleep(0.05)
        timer()
    else:
        while count_red > 0 and count_red < 1500:
            if len(listo_red) > 0:
                create_red()
                process_input()
                immune_response()
                time.sleep(0.05)
                Canvas_1.update()
        break

window.mainloop()
