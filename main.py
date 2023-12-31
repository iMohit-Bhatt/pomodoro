from tkinter import *
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer)
    title_label.config(text="TIMER")
    canvas.itemconfig(timer_text, text='00:00')
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 



def start():
    global reps 
    reps += 1

    work_sec = WORK_MIN * 60
    SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
    LONG_BREAK_SEC = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(LONG_BREAK_SEC)
        title_label.config(text= 'BREAK', fg=RED)

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_SEC)
        title_label.config(text='BREAK', fg=PINK)

    else:   
        count_down(work_sec)
        title_label.config(text='WORK', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60

    if sec == 0:
        sec = "00"
        
    elif sec <= 9 and sec > 0:
        canvas.itemconfig(timer_text, text=f"{min}:0{sec}")
        
    else:
        canvas.itemconfig(timer_text, text=f"{min}:{sec}")

    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start()
        mark = ""
        Work_Session = math.floor(reps/2)
        for _ in range(Work_Session):
            mark += "✓"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row= 1)

start_btn = Button(text='Start', command=start, highlightthickness=0, bg= YELLOW)
start_btn.grid(column=0, row=2)

reset_btn = Button(text='Reset', highlightthickness=0, command=reset, bg= YELLOW)
reset_btn.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_mark.grid(column=1, row=3)

window.mainloop()