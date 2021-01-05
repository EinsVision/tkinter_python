from tkinter import *
root = Tk()
root.title('ThorDrive GUI')
root.geometry('640x480')

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, '글자를 입력하세요.')

ent = Entry(root, width=30)
ent.pack()
ent.insert(0, '한줄 만입력하세요.')

def btncmd():
    # 내용 출력
    print(txt.get('1.0', END)) # 1: 첫번째 라인, 0: column 위치
    print(ent.get())

    # 내용 삭제
    txt.delete('1.0', END)
    ent.delete(0, END)

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()