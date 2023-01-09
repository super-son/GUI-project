from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# btn1.pack()
# btn2.pack()

# btn1.pack(side="left")
# btn2.pack(side="right")

# 팩은 쌓는 느낌이라면 그리드는 좌표에 대입하는 것
# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

# 맨 윗줄
# ... width=5, height=2) #패딩 값을 부여대신 같은 넓이를 주기위해서 절대적인 수치사용
# padding값으로 일괄처리하면 텍스트길이 긴애들 때메 버튼 길이가 행마다 다르거든..
btn_f16 = Button(root, text="F16", width=5, height=2) 
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

#sticky news는 동서남북 방향으로 늘린다는 뜻!, w만 적는다면 서쪽으로만 붙인다는 뜻이지
btn_f16.grid(row=0,column=0, sticky=N+E+W+S, padx=3, pady=3) #버튼간에 간격을 주기위함
btn_f17.grid(row=0,column=1, sticky=N+E+W+S, padx=3, pady=3) 
btn_f18.grid(row=0,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0,column=3, sticky=N+E+W+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 7시작줄
btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_diff = Button(root, text="-", width=5, height=2)

btn_7.grid(row=2,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_diff.grid(row=2,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4시작줄
btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_plus = Button(root, text="+", width=5, height=2)

btn_4.grid(row=3,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_plus.grid(row=3,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 1시작줄
btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2) #세로 2칸씀

btn_1.grid(row=4,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4,column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) #현재 위치로 부터 아래쪽으로 칸을 더함

# 0시작줄
btn_0 = Button(root, text="0", width=5, height=2) #가로 2칸씀
btn_dot = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5,column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) #현재 위치로 부터 오른쪽으로 칸을 더함
btn_dot.grid(row=5,column=2, sticky=N+E+W+S, padx=3, pady=3)


root.mainloop() 


