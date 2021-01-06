import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('ThorDrive GUI')
root.geometry('640x480')

def info():
    msgbox.showinfo('알림', '정상적으로 예매 완료되었습니다.')

def warning():
    msgbox.showwarning('경고', '예매가 취소 되었습니다.')

def error():
    msgbox.showerror('에러', '에러가 발생했습니다.')

def okcancel():
    msgbox.askokcancel('확인 / 취소', '해당 좌석은 유아동반석입니다. 예매하시겠습니까?')

def retrycancel():
    msgbox.askretrycancel('재시도 / 취소', '일시적인 오류입니다. 재시도하시겠습니까?')

def yesno():
    msgbox.askyesno('확인 / 취소','해당 좌석은 역방향입니다. 예매하시겠습니까?')

def yesnocancel():
    response = msgbox.askyesnocancel('확인 / 취소','해당 좌석은 역방향입니다. 예매하시겠습니까?')
    print(response)

    if response == 1:
        print('예')

    elif response == 0:
        print('아니오')

    else :
        print('그냥 취소')

# pop-up window를 띄우는 것이다.
Button(root, command=info, text='알림').pack()
Button(root, command=warning, text='경고').pack()
Button(root, command=error, text='에러').pack()
Button(root, command=okcancel, text='확인 취소').pack()
Button(root, command=retrycancel, text='재시도 취소').pack()
Button(root, command=yesno, text='재시도 취소').pack()
Button(root, command=yesnocancel, text='재시도 취소').pack()

root.mainloop()