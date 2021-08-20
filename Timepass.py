import pyautogui as pi
import time
import subprocess as sp
import tkinter as tk

screen = tk.Tk()
screen.title("Time Pass")
screen.configure(bg="black")

x = {'Cooku With Comali': 'https://www.hotstar.com/in/tv/cooku-withh-comali/1260013771',
     'KPY S5': 'https://www.hotstar.com/in/tv/kalakka-povadhu-yaaru/4883/seasons/season-5/',
     'KPY S6': 'https://www.hotstar.com/in/tv/kalakka-povadhu-yaaru/4883/seasons/season-6/ss-2381',
     'Youtube': 'https://www.youtube.com/',
     'Udemy': 'https://www.udemy.com/home/my-courses/learning/'
     }
def open(p):
    sp.run("brave")
    time.sleep(2)
    if (p == 1):
        pi.write(x.get("Cooku With Comali"))
        pi.press('enter')
    if (p == 2):
        pi.write(x.get("KPY S5"))
        pi.press('enter')
    if (p == 3):
        pi.write(x.get("KPY S6"))
        pi.press('enter')
    if (p == 4):
        pi.write(x.get("Youtube"))
        pi.press('enter')
    if (p == 5):
        pi.write(x.get("Udemy"))
        pi.press('enter')


def button():
    b1 = tk.Button(screen, text="Cooku With Comali", command=lambda: open(1), height=1, width=30,font="none 16 bold italic")
    b2 = tk.Button(screen, text="KPY S5", command=lambda: open(2), height=1, width=30,font="none 16 bold italic")
    b3 = tk.Button(screen, text="KPY S6", command=lambda: open(3), height=1, width=30,font="none 16 bold italic")
    b4 = tk.Button(screen, text="Youtube", command=lambda: open(4), height=1, width=30,font="none 16 bold italic")
    b5 = tk.Button(screen, text="Udemy", command=lambda: open(5), height=1, width=30,font="none 16 bold italic")

    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()

button()
screen.mainloop()

