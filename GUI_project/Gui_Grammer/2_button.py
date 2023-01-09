from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack() #해줘야 버튼이 보인다

btn2 = Button(root, padx=5, pady=10, text="버튼22222222222")
btn2.pack() #글짜를 기준으로 패딩값이라 보면될듯

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼44444444444")
btn4.pack() #고정적인 크기

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack() #글자색과 배경색

photo = PhotoImage(file=r"C:\Users\hj144\Desktop\Coding\Python\GUI_project\Gui_Grammer\3_images\check.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd) #btncmd는 내가 임의로 지은거
btn7.pack()

root.mainloop() #루프를 통해 창이 닫히지 않도록

