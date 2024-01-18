# ---------------------------- IMPORTS ------------------------------- #

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
resp = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def enable_start_button():
    start_button.config(state=NORMAL)

def reset_timer():
    global resp
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    resp = 0
    check_marks.config(text="")
    enable_start_button()

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global resp, timer
    
    # Disabilita il pulsante Start dopo la prima pressione
    start_button.config(state=DISABLED)
    
    work_sec = int(work_spinbox.get()) * 60
    short_break_sec = int(short_break_spinbox.get()) * 60
    long_break_sec = int(long_break_spinbox.get()) * 60
    
    resp += 1
    
    if resp % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif resp % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_sec <= 9:
        count_sec = "0"+str(count_sec)
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()    
        check_marks_holder = math.ceil(resp / 2)*"✔"
        check_marks.config(text=check_marks_holder)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


work_label = Label(text="Work Time:", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12))
work_label.grid(column=0, row=1)

short_break_label = Label(text="Short Break Time:", bg=YELLOW, fg=PINK, font=(FONT_NAME, 12))
short_break_label.grid(column=1, row=1)

long_break_label = Label(text="Long Break Time:", bg=YELLOW, fg=RED, font=(FONT_NAME, 12))
long_break_label.grid(column=2, row=1)

# Spinbox per le opzioni
work_spinbox = Spinbox(from_=1, to=60, width=10)
work_spinbox.grid(column=0, row=3)

short_break_spinbox = Spinbox(from_=1, to=60, width=10)
short_break_spinbox.grid(column=1, row=3)

long_break_spinbox = Spinbox(from_=1, to=60, width=10)
long_break_spinbox.grid(column=2, row=3)

# Tomato Image definition
canvas = Canvas(width=202, height=226, background=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100.5, 112, image=tomatoImg)
timer_text = canvas.create_text(102, 134, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=4, pady=20)




 
start_button = Button(text="Start", highlightthickness=0, command=start_timer, height=2, width=10)
start_button.grid(column=0, row=5)


reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, height=2, width=10)
reset_button.grid(column=2, row=5)


check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2, pady=10)


window.mainloop()

