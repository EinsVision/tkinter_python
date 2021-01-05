from tkinter import *
root = Tk()
root.title('ThorDrive GUI')
root.geometry('640x480')

listbox = Listbox(root, selectmode='extended', height=0)
listbox.insert(0,'사과')
listbox.insert(1,'딸기')
listbox.insert(2,'바나나')
listbox.insert(END,'수박')
listbox.insert(END,'포도')
listbox.pack()

def btncmd():
    # listbox.delete(END) # 맨뒤에 항목을 삭제한다.
    listbox.delete(0)
    print('리스트에는', listbox.size(), ' 개가 있어요.')
    print('항목 출력하기', listbox.get(0,2))
    print('선택된 항목', listbox.curselection())

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()