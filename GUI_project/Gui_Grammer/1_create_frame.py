from tkinter import *

root = Tk()
root.title("Nado GUI")
# root.geometry("640x480") #X도 안되고 *도 안되, 가로세로설정
root.geometry("640x480+100+300") #가로*세로+x좌표+y좌표라는 뜻, 0,0은 젤 왼쪽위


root.resizable(False, False) #x(너비), y(높이) 값 변경 불가(창 크기 맘대로 조절못해)


root.mainloop() #루프를 통해 창이 닫히지 않도록

