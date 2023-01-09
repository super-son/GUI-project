from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt=Text(root, width=30, height=5) #여러 줄 입력가능
txt.pack()
txt.insert(END, "글자를 입력하세요") #0으로는 오류나네..


e=Entry(root, width=30) #엔터를 못쳐서 한줄만 입력가능
e.pack() #Ex): 아이디입력창
e.insert(0, "한 줄만 입력해요")#처음위치에 기본값이 들어간는 것,  
#현재는 값이 비어 있어서 end써도 동일

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) #처음부터 끝까지 모든 텍스트 가져오는것
    #1은 라인 1부터, 0은 0번째 인덱스부터 쭉
    print(e.get()) # ㅋ위에서 e=Entry(root, width=30).pack() 이런식으로 만들면 get을 못받네 ㅋㅋㅋㅋ 걍 pack 따로쓰자

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() 

