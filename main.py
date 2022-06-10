from tkinter import *
import math
import pygame

RED = "#F24C4C"
WORK = 25*60
SHORT_BREAK = 5*60
LONG_BREAK = 30*60
REPS = 0
timer = None
mark = ""
pygame.mixer.init()


# RESET TIMER
def reset_timer():
    window.after_cancel(timer)
    global REPS
    REPS = 0
    canvas.itemconfig(timer_text, text=f"00:00")
    main_label.config(text="TIMER")
    pomodoro_count.config(text="")




# TODO: SET A PAUSE FUNCTION




# PLAY ALARM SOUND
def play():
    pygame.mixer.music.load('alarm.mp3')
    pygame.mixer.music.play(loops=0)


# START TIMER
def start_timer():
    global REPS
    REPS += 1

    if REPS % 2 == 1:
        count_down(WORK)
        main_label.config(text="WORK")
    elif REPS % 8 == 0:
        count_down(LONG_BREAK)
        main_label.config(text="LONG-BREAK")
        play()
    else:
        count_down(SHORT_BREAK)
        main_label.config(text="SHORT-BREAK")
        play()


# START COUNTDOWN
def count_down(count):
    count_min = math.floor(count/60)
    count_seg = count % 60

    if count_seg <= 9:
        count_seg = f"0{count_seg}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seg}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if REPS % 2 == 0:
            global mark
            mark += "X"
            if REPS % 8 == 0:
                mark += " | "
            pomodoro_count.config(text=mark)


# CONFIGURATION OF TK WINDOW
window = Tk()
window.title("Pomodoro")
window.config(padx=70, pady=50, bg=RED)
window.minsize(width=500, height=400)
window.resizable(False, False)

canvas = Canvas(width=300, height=200, bg=RED, highlightthickness=0)
tomato_img = PhotoImage(file="POM2.png")
canvas.create_image(150, 30, image=tomato_img)
timer_text = canvas.create_text(150, 150, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.grid(column=1,row=1)

main_label = Label(text="TIMER", font=("Arial", 24, "bold"))
main_label.grid(column=1, row=3, padx=20, pady=20)
main_label.config(bg=RED, fg="white")


button_start = Button(text="START", command=start_timer)
button_start.grid(column=0, row=1)


button_reset = Button(text="RESET", command=reset_timer)
button_reset.grid(column=2, row=1)

pomodoro_count = Label(fg="white", bg=RED, font=("Arial", 16, "normal"))
pomodoro_count.grid(column=1, row=5)


window.mainloop()
