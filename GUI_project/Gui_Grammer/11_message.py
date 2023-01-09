import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

#기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo("알림","정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고","해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러","결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소","해당 좌석은 유아동반석입니다 예매하시겠습니까?")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소","일시적인 오류입니다. 다시 시도하시겠습니까?")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel(): # 속성이름적고 =none으로 흘리기 기술.. 개꿀팁, 근데 속성이름 한번언급해서 뒤에속성도 적어줘야 되는듯 #위 형식이랑 똑같이해도되네
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장하시겠습니까?")
    # response 변수로 받음으로써 사용자의 응답을 받기위함
    #네 : 저장 후 종료
    #아니오 : 저장 하지 않고 종료
    #취소 : 프로그램 종료 취소(현재 화면에서 계속 작업)
    print("응답:",response) # 값이 어떻게 나오나 보기위해서.. 보통 True, False, None 나온데
    #이때 예=1, 아니오=0, 그 외 이렇게 생각
    if response ==1: # 예 인 상황
        print("예")
    elif response ==0:
        print("아니오")
    else:
        print("취소")
    
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인/취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()


root.mainloop() 


