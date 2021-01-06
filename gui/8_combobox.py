import tkinter.ttk as ttk

from tkinter import *
root = Tk()
root.title('ThorDrive GUI')
root.geometry('640x480')

values = [str(i)+ '일' for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set('카드 결제일')

readOnly_combobox = ttk.Combobox(root, height=10, values=values, state='readonly')
readOnly_combobox.pack()
readOnly_combobox.current(0)

def btncmd():
    print(combobox.get())
    print(readOnly_combobox.get())

btn = Button(root, text='select', command=btncmd)
btn.pack()

root.mainloop()