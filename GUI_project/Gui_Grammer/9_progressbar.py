import tkinter.ttk as ttk 
import time
from tkinter import *
#프로그레스바는 다운로드 진행상태 5%라던지 그럴때 이용

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") #애는 막대가 왓다리 갓다리
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") #애는 게이지채우기
# progressbar.start(10) #10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() #작동중지


# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

# 이번에는 진짜 진행상태에 따른 게이지 움직임을 보여주지

p_var2 = DoubleVar() #실수값도 반영하기위해서 더블을 사용
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2) #length는 게이지 길이
progressbar2.pack()

def btncmd2():
    for i in range(1,101): #1부터 100
        time.sleep(0.01) #0.01초 대기 

        p_var2.set(i) #progress bar의 값 설정
        progressbar2.update() #ui 업데이트
        print(p_var2.get()) 

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop() 

