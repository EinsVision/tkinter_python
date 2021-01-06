from tkinter import *

root = Tk()
root.title('ThorDrive GUI')
root.geometry('640x480')

def create_new_file():
    print('새 파일을 만듭니다.')

menu = Menu(root)

#file menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='New File', command=create_new_file)
menu_file.add_command(label='New Window')
menu_file.add_separator()
menu_file.add_command(label='Open File')
menu_file.add_separator()
menu_file.add_command(label='Save All', state='disable') # 비활성화
menu_file.add_separator()
menu_file.add_command(label='Exit', command=root.quit)

menu.add_cascade(label='File', menu=menu_file)

#edit menu
menu.add_cascade(label='Edit')

# Language menu 추가
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='Python')
menu_lang.add_radiobutton(label='C')
menu_lang.add_radiobutton(label='Javascript')
menu.add_cascade(label='language', menu=menu_lang)

root.config(menu=menu)
root.mainloop()