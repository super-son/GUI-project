from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root,text="메뉴를 선택해 주세요").pack(side="top")
Button(root, text="주문하기").pack(side="bottom")
# 버거 프레임

#relief는 테두리 모양, bd는 외곽선 표시
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True) #fill="x"하면 x축 방향으로 채우기임
#왼쪽으로 옮기고, 높이꽉차게하고, 패딩을 부풀린다

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 음료 프레임

frame_drink = LabelFrame(root, text="음료", relief="solid", bd=1) 
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop() 


