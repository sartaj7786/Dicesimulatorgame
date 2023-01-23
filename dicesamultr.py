from tkinter import*
import random

window = Tk()
window.minsize(600,600)
window.maxsize(500,500)
window.title('ROOL DICE')

label = Label(window,font=('bold',300))

def roll():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text=f'{random.choice(number)}')
    label.pack()


heading = Label(window,text='ROLL THE DICE',font=('bold',50),bg='light cyan')
heading.pack(fill=X)


button = Button(window,text='Roll',font=('normal',25),command=lambda:roll())
button.pack()
window.mainloop()
