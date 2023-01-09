from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

#single 모드는 한개 선택가능
#extended 모드는 여러개 선택가능 #여러 줄에 거쳐 목록관리
listbox = Listbox(root, selectmode="extended", height=0) #0적으면 다보여주는거 3적으면 위에서 3개만 보여주는거
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    #삭제
    # listbox.delete(END) #클릭시 맨뒤 항목 삭제, 0이면 맨 앞부터 

    #갯수 확인
    # print("리스트에는", listbox.size(),"개가 있어요")
    # print("리스트에는", str(listbox.size())+"개가 있어요") #띄어쓰기 없애기

    #항목 확인 get(0,2)는 첫번째인덱스부터 셋째까지 인덱스를 출력할꺼다
    print("1번째부터 3번째까지의 항목 :", listbox.get(0,2))
    
    #현재 선택된 항목 확인, 위치로 변환
    print("선택된 항목 : ", listbox.curselection())

    #그럼 선택된 항목들 모두 항목이름으로 출력해보자. 실습완료
    a1=listbox.curselection()[0]
    a2=listbox.curselection()[2]
    print("선택된 항목 : ", listbox.get(a1,a2))

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() 

