from tkinter import *
from tkinter import messagebox

window = Tk() # 윈도우 객체 생성

# 창 이름 설정
window.title('GUI 프로그램')
# 창 크기 및 위치 설정 
window.geometry('300x500+100+200')
# '너비x높이+x좌표+y좌표'

# 창 크기 고정
window.resizable(False, False)
# 좌우(True/False), 상하(True/False)
# False : 크기 고정(변경 X)
# True : 크기 변경 가능

text = ""
# 버튼 이벤트 처리 함수
def onClick():
    text = entry1.get()
    print(type(text))
    messagebox.showinfo("알림", text)
    
def sel_chk():
    if ck1val.get() == 1 and ck2val.get() == 1:
        messagebox.showinfo('선택', '모두 선택')
    elif ck2val.get() == 1:
        messagebox.showinfo('선택', '고양이를 선택')
    elif ck1val.get() == 1:
        messagebox.showinfo('선택', '강아지를 선택')

def sel_rd():
    if rd_val.get() == 0:
        messagebox.showinfo('선택', '자장면 선택')
    elif rd_val.get() == 1:
        messagebox.showinfo('선택', '짬뽕 선택')
    else:
        messagebox.showinfo('선택', '볶음밥 선택')

# 위젯 활용
label1 = Label(window, text='안녕하세요~', fg="indian red", bg='dark slate gray')
label1.pack()

btn1 = Button(window, text='눌러', width=20, fg='blue', command=onClick)
btn1.pack()

entry1 = Entry(window)
entry1.pack()

list1 = Listbox(window, selectmode='multiple')
list1.insert(0, '1번')
list1.insert(1, '2번')
list1.insert(2, '3번')
list1.insert(3, '4번')
# list1.delete(2)
list1.pack()

ck1val = IntVar()
ck1 = Checkbutton(window, text='강아지', variable=ck1val)
ck2val = IntVar()
ck2 = Checkbutton(window, text='고양이', variable=ck2val)
ck1.pack()
ck2.pack()

btn2 = Button(window, text='선택', command=sel_chk)
btn2.pack()

rd_val = IntVar()
rd1 = Radiobutton(window, text='자장면', variable=rd_val, value=0, command=sel_rd)
rd2 = Radiobutton(window, text='짬뽕', variable=rd_val, value=1, command=sel_rd)
rd3 = Radiobutton(window, text='볶음밥', variable=rd_val, value=2, command=sel_rd)
rd1.pack()
rd2.pack()
rd3.pack()

# 실행
window.mainloop()