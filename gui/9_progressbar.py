import tkinter.ttk as ttk
import time
from tkinter import *
root = Tk()
root.title('ThorDrive GUI')
root.geometry('640x480')

# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate') # progressbar 가 결정되지 않은 상태를 얘기한다.
# progressbar = ttk.Progressbar(root, maximum=100, mode='determinate') 
# progressbar.start(10)
# progressbar.pack()

# def btncmd():
#     progressbar.stop()

# btn = Button(root, text='stop', command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)
        p_var2.set(i)
        progressbar2.update()
        print(p_var2.get())

btn = Button(root, text='시작', command=btncmd2)
btn.pack()

root.mainloop()