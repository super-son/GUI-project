from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

Scrollbar = Scrollbar(frame)
Scrollbar.pack(side="right", fill="y")

#set이 없으면 스크롤을 내려도 다시 올라옴. fix가 안되구만~. 모드를 single로 설정하면 중복선택 불가능
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = Scrollbar.set)

for i in range(1,32):
    listbox.insert(END, str(i)+"일") #1일, 2일..
listbox.pack(side="left")

#이 과정까지 해줘야 서로 mapping이 된다
Scrollbar.config(command=listbox.yview)

root.mainloop() 


