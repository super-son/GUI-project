import os
from tkinter import *

root = Tk()
root.title("*제목 없음 - Windows 메모장")
root.geometry("640x480+100+300")
root.resizable(True,True)

# 열기, 저장 파일 이름
filename="mynote.txt"

def Load():
    if os.path.isfile(filename) : #파일 있으면 true
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) #있던 내용은 다 지워버리고
            txt.insert(END, file.read())
        root.title(filename)

def Save():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 첫번째 라인의 0인덱스의 칼럼에서부터 끝까지 다 가져온다

# 스크롤 바
scroll = Scrollbar(root)
scroll.pack(side="right", fill="y") # "y" 쓰거나 Y 이렇게 써두 무방
 
# 텍스트 화면 + 매핑
txt = Text(root,yscrollcommand=scroll.set)
txt.pack(side="left", fill="both", expand=True)
scroll.config(command=txt.yview)


menu = Menu(root)

#파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=Load)
menu_file.add_command(label="저장", command=Save)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit) 
menu.add_cascade(label="파일", menu=menu_file)

#그 외 메뉴 (빈 값)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.config(menu=menu)
root.mainloop() 