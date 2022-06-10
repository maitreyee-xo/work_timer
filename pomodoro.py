import tkinter
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

def reset_timer():
    window.after_cancel(label_1) # cancels timer set up previously
    canvas.itemconfig(timertext, text="00:00")
    label_1.config(text="Timer")
    label_2.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def starttimer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        countdown(short_break_sec)
        label_1.config(text = "Short Break", fg = PINK)

    elif reps % 8 == 0:
        countdown(long_break_sec)
        label_1.config(text = "Long Break", fg = RED)
    else:
        countdown(work_sec)
        label_1.config(text = "Work", fg = GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min == 0 and count_sec < 10:
        count_sec = f"0{count}"

    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timertext, text=f"{count_min}:{count_sec}", )
    if count > 0:
        timer = window.after(1000, countdown, count - 1)

    else:
        starttimer()
        m = ""
        for _ in range(math.floor(reps/2)):
            m +="✅"
        label_2.config(text = m)





# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_1 = tkinter.Label(text="Timer", font=("Courier", 24, "bold"), bg=YELLOW, fg=GREEN)
label_1.grid(row=0, column=1)
label_2 = tkinter.Label()
label_2.grid(row=4, column=1)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatina_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatina_img)
timertext = canvas.create_text(102, 129, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.grid(row=1, column=1)
button_1 = tkinter.Button(text="Start", font=("Arial", 8, "normal"), command=starttimer)
# button_1.config(height = 1, width = 1)
button_1.grid(row=3, column=0)
button_2 = tkinter.Button(text="Reset", font=("Arial", 8, "normal"), command = reset_timer)
button_2.grid(row=3, column=2)

window.mainloop()
