from tkinter import *
import textwrap
# text파일은 자동줄바꿈이 자꾸추가되어서 뭘 할려해도 자꾸 꼬인다
#그래서 줄바꿈제거기능(textwrap)을 쓰거나 entry를 이용해야할듯

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame_small = Frame(root, relief="solid", bd=2)
frame_small.pack() #side="left"나 "right"안 적혀있어서 중앙배정인듯
frame_big = Frame(root, relief="solid", bd=3)
frame_big.pack()

entry_value = StringVar(root, value='')
txt=Entry(frame_small, width=29, textvariable = entry_value) #여러 줄 입력가능
txt.pack()


def inner_7():
    if txt.get()=="+": # text에서는그냥 +여서 안되는거엿네 엌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ레전드 "+\n"
        txt.delete(0, END)
        txt.insert(END,7)
    else :
        txt.insert(END,7)

def inner_8():
    if txt.get()=="+":
        txt.delete(0, END)
        txt.insert(END,8)
    else :
        txt.insert(END,8)   

def inner_plus():
    global front_txt
    front_txt=txt.get()
    txt.delete(0, END)
    txt.insert(END,"+")
    global vohu
    vohu="+"
    #return을 하면 if inner_plus()=3 이런식의 문장에서도 함수가 재작동하기때문에 사용하지않는거네
    #내가 봤을때는 global같은 거 최대한 지양하려면 cal_result하나로 묶은다음에 거기서 하위로 가는식으로
    #코드를 구성해야지 싶네. global은 정말 어쩔수없을때만 쓸듯.

def cal_result():
    back_txt=txt.get()
    txt.delete(0, END)
    if vohu=="+":
        real_result = int(front_txt) + int(back_txt)
        txt.insert(END, real_result)
    return

btn_f16 = Button(frame_big, text="F16", width=5, height=2) 
btn_f17 = Button(frame_big, text="F17", width=5, height=2)
btn_f18 = Button(frame_big, text="F18", width=5, height=2)
btn_f19 = Button(frame_big, text="F19", width=5, height=2)

#sticky news는 동서남북 방향으로 늘린다는 뜻!, w만 적는다면 서쪽으로만 붙인다는 뜻이지
btn_f16.grid(row=0,column=0, sticky=N+E+W+S, padx=3, pady=3) #버튼간에 간격을 주기위함
btn_f17.grid(row=0,column=1, sticky=N+E+W+S, padx=3, pady=3) 
btn_f18.grid(row=0,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0,column=3, sticky=N+E+W+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(frame_big, text="clear", width=5, height=2)
btn_equal = Button(frame_big, text="=", width=5, height=2)
btn_div = Button(frame_big, text="/", width=5, height=2)
btn_mul = Button(frame_big, text="*", width=5, height=2)

btn_clear.grid(row=1,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 7시작줄
btn_7 = Button(frame_big, text="7", width=5, height=2, command=inner_7)
btn_8 = Button(frame_big, text="8", width=5, height=2, command=inner_8)
btn_9 = Button(frame_big, text="9", width=5, height=2)
btn_diff = Button(frame_big, text="-", width=5, height=2)

btn_7.grid(row=2,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_diff.grid(row=2,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4시작줄
btn_4 = Button(frame_big, text="4", width=5, height=2)
btn_5 = Button(frame_big, text="5", width=5, height=2)
btn_6 = Button(frame_big, text="6", width=5, height=2)
btn_plus = Button(frame_big, text="+", width=5, height=2, command=inner_plus)

btn_4.grid(row=3,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_plus.grid(row=3,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 1시작줄
btn_1 = Button(frame_big, text="1", width=5, height=2)
btn_2 = Button(frame_big, text="2", width=5, height=2)
btn_3 = Button(frame_big, text="3", width=5, height=2)
btn_enter = Button(frame_big, text="enter", width=5, height=2, command=cal_result) #세로 2칸씀

btn_1.grid(row=4,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4,column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) #현재 위치로 부터 아래쪽으로 칸을 더함

# 0시작줄
btn_0 = Button(frame_big, text="0", width=5, height=2) #가로 2칸씀
btn_dot = Button(frame_big, text=".", width=5, height=2)

btn_0.grid(row=5,column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) #현재 위치로 부터 오른쪽으로 칸을 더함
btn_dot.grid(row=5,column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop() 


