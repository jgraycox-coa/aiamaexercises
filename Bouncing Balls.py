import tkinter as tk
import random
import time
import sched


CANVAS_SIZE = 600
WIDTH = 3
NUM_BALLS = 70
COLOR = ['yellow', 'green', 'red', 'blue', 'pink']
dirs = []

def go():
    global dirs
    global COLOR
    global WIDTH
    play = lambda: PlaySound('Sound.wav', SND_FILENAME)
    for i in range(NUM_BALLS):
        x = random.randint(WIDTH, CANVAS_SIZE - WIDTH)
        y = random.randint(WIDTH, CANVAS_SIZE - WIDTH)
        canvas.create_oval(x, y, x + WIDTH, y + WIDTH, fill = COLOR[i])
        dirs.append([random.randint(-3, 3), random.randint(-3, 3)])
        COLOR.append([COLOR[i]])
        if WIDTH < 60:
            WIDTH += 1
        else:
            WIDTH += 10
    balls = canvas.find_all()
    print(balls)
    while True:
        for i in range(len(balls)):
            canvas.move(balls[i], dirs[i][0], dirs[i][1])

            coords = canvas.coords(balls[i])
            if coords[0] <= 0:
                dirs[i][0] = -dirs[i][0]
            if coords[1] <= 0:
                dirs[i][1] = -dirs[i][1]
            if coords[2] >= CANVAS_SIZE:
               dirs[i][0] = -dirs[i][0]
               play
            if coords[3] >= CANVAS_SIZE:
                dirs[i][1] = -dirs[i][1]
                play
        
        window.update()
        time.sleep(0.01)

def periodic(scheduler, interval, action, actionargs=()):
    scheduler.enter(interval, 1, periodic,
                    (scheduler, interval, action, actionargs))
    action(*actionargs)

# Main Program
window = tk.Tk()
window.title("Bouncing Balls")
canvas = tk.Canvas(window, width = CANVAS_SIZE, height = CANVAS_SIZE,
                    bg = 'black')

btnGo = tk.Button(window, text = "Go!", command = go)

canvas.grid(row = 0, column = 0)
btnGo.grid(row = 1, column = 0)



window.mainloop()


