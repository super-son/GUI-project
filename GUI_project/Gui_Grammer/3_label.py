#레이블은 실제로 동작을 하거나 하는건아니고
#글자나 이미지를 보여준다
from tkinter import *
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file=resource_path(r"3_images\check.png")) #원래 절대경로 했었는데 이렇게 연습좀요.
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")  #위의 안녕하세요 텍스트를 변경
    
    global photo2
    photo2 = PhotoImage(file=resource_path(r"3_images\cancel.png"))
    label2.config(image=photo2)
    #garbage collection(불필요한 메모리 공간해제) 얘가 photo2 변수를 잡아먹어치워서
    #따로 전역변수로 만들어줘야한다
    #photo를 변경시킬때 전역변수 사용한다는걸 유념하자 

btn=Button(root, text="클릭", command=change)
btn.pack()

root.mainloop() 

