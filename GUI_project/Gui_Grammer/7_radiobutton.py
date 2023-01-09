#4개 보기 중 하나를 선택. 이를 라디오 버튼이라 칭함
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="메뉴를 선택하세요").pack() #이렇게 pack을 뒤에 붙여도 가능

burger_var = IntVar() #인트형으로 값을 저장
btn_burger1 =Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select() #미리선택
btn_burger2 =Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 =Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label1 = Label(root, text="음료를 선택하세요").pack() #이렇게 pack을 뒤에 붙여도 가능

drink_var=StringVar() #스트링형으로 값을 저장
btn_drink1= Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select() #기본값 선택
btn_drink2= Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) #선택된 라디오 항목의 값(vaule) 반환
    print(drink_var.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop() 

