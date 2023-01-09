from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

#File 메뉴
menu_file = Menu(menu, tearoff=0) # tearoff 하니까 점선같은게 사라지네
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) 
menu.add_cascade(label="File", menu=menu_file)
#menu file의 정보가 menu에 들어가고 File로 정의되는 것이다

#Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

#Language 메뉴 추가(radio 버튼을 통해서 택1)
menu_lang = Menu(menu,tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# view 메뉴 #애는 혼자라서 라디오아니고 체크ㄱㄴ
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu) #이게 꼭 들어가저야 하구나
root.mainloop() 


