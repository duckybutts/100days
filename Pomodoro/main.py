from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkMarks = ""
times = None
running = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    global checkMarks
    global running

    running = False

    window.after_cancel(times)
    reps = 0
    checkMarks = ""
    check.config(text=f"{checkMarks}", fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer, text="00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    global checkMarks
    global running

    if running:
        return
    running = True

    reps += 1
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    work = WORK_MIN * 60

    title.config(text="Work", fg="GREEN")
    countDown(work)
    if (reps % 8 == 0) :
        title.config(text="Long Break", fg="RED")
        countDown(long_break)
    elif (reps % 2 == 0) :
        title.config(text="Break", fg="PINK")
        countDown(short_break)
        checkMarks += "✅"
        check.config(text=f"{checkMarks}", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countDown(count):
    global reps
    global times

    count_min = math.floor(count/60)
    count_sec = count % 60
    if ((count_sec == 0) or (count < 10)):
        count_sec = f"0{count_sec}"     # dynamic typing

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        times = window.after(1000, countDown, count - 1)
    else:
        start()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(150, 120, image=tomatoImg)
timer = canvas.create_text(150, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)
title = Label(text="Timer", fg=GREEN,  bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title.grid(column=1, row=1, pady=20)
check = Label(text= f"{checkMarks}", fg=GREEN, bg=YELLOW)
check.grid(column=1, row=4)
start = Button(text="Start", command=start,  highlightbackground=YELLOW)
start.grid(column=0, row=3)
reset = Button(text="Reset", command=reset,  highlightbackground=YELLOW)
reset.grid(column=2, row=3)

window.mainloop()
