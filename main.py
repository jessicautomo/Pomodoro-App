from tkinter import *
import time as t
#from playsound import playsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro ✰")
window.config(padx=100, pady=50, bg=YELLOW) #padding to make space outside of the canvas

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0) #highlightthickness is basically border thickness
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img) #first two arguments are for position(middle of 200 and 224, to place it in the middle of the canvas)
timer = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=3,column=2)

timer_label = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,40,"bold"))
timer_label.grid(column=2,row=1)

status_label = Label(text="",bg=YELLOW,fg=GREEN,font=(FONT_NAME,13,"bold"))
status_label.grid(column=2,row=2)

check_label = Label(text="",bg=YELLOW,fg=GREEN,font=(FONT_NAME,20))
check_label.grid(row=5,column=2)

def time_countdown():
    global time
    for i in range(time+1):
        time -= 1
        sec = time%60
        min = int(time / 60)
        if sec < 10:
            sec_display = f"0{sec}"
        else:
            sec_display = sec
        if min < 10:
            min_display = f"0{min}"
        else:
            min_display = min
        window.update()
        t.sleep(0.001)
        if time > 0:
            canvas.itemconfig(timer,text=f"{min_display}:{sec_display}")
        elif time == 0:
            canvas.itemconfig(timer, text="00:00")

def start():
    work_session = 0
    time=0
    def one_work_session():
        global time
        time = 60*WORK_MIN
        time_countdown()

    def one_break():
        global time
        if work_session == 4:
            time = 60*LONG_BREAK_MIN
        else:
            time = 60*SHORT_BREAK_MIN
        time_countdown()

    for i in range(4):
        if work_session == 0:
            status_label.config(text="time to get to work")
        elif work_session == 1:
            status_label.config(text="keep it up girl!")
        elif work_session == 2:
            status_label.config(text="ur doing super well")
        else:
            status_label.config(text="almost there - you got this <3")
        one_work_session()
        #playsound("Ding Sound Effect.mp3")
        work_session += 1
        if work_session == 1:
            check_label.config(text="✔")
            status_label.config(text="good work! take a break ^^")
        elif work_session == 2:
            check_label.config(text="✔✔")
            status_label.config(text="take a breather")
        elif work_session == 3:
            check_label.config(text="✔✔✔")
            status_label.config(text="cool down for a sec")
        else:
            check_label.config(text="✔✔✔✔")
            status_label.config(text="you've done 1hr and 40mins of work! give yourself a pat in the back and recharge for a little :)")
            t.sleep(30)
            status_label.config(text="")
        one_break()
        t.sleep(10)
        #playsound("Ding Sound Effect.mp3") --> doesn't work, cannot initialize MCI

start_button = Button(text="Start",command=start,highlightthickness=0)
start_button.grid(row=4,column=1)

def reset():
    global time
    time = 0
    canvas.itemconfig(timer,text="00:00")
    check_label.config(text="")
    status_label.config(text="")

reset_button = Button(text="Reset",command=reset,highlightthickness=0)
reset_button.grid(row=4,column=3)

window.mainloop()