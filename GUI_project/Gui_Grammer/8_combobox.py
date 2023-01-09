import tkinter.ttk as ttk #콤보박스를 사용하기위해 #tkinter파일안 .pyi파일중하나는 이렇게 따로 임포트하는듯
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

#콤보 박스에 글이 입력됨 ㅋ
values = [str(i) + "일" for i in range(1,32)] #1부터 31까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack() #height는 목록펼치기해서 나오는 개수
combobox.set("카드 결제일") #최초 목록 제목 설정

#콤보 박스에 글자 입력못하게
readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") #읽기
readonly_combobox.current(0) #0번째 인덱스값 첨에 보이게 선택
readonly_combobox.pack() 

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop() 

