#여러크기의 위젯 등이 혼합되어있기때문에 그리드가 아닌 팩을 쓰겠다
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * #__all__ 여기다가 정의하지않으면 그 서브모듈에 대해서는 따로 임포트하지않아
from tkinter import filedialog #그래서 별도로 임포트해준다
#무조건 해줘야 되는 과정이었네.. 공부요망
from PIL import Image
import os

root = Tk()
root.title("Image-Pro")

# 파일 추가 func
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")),
        initialdir=r"Desktop:/*") # 최초의 경로를 설정해줌

    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)

# 선택 삭제 func
def del_file():
    # print(list_file.curselection()) # 처리내용확인
    for index in reversed(list_file.curselection()):
    # 리버스로 거꾸로 뽑아야 인덱스 순서가 안밀리고 제대로 삭제되지 ㅎ
    # 그렇다고 리스트배열 자체가 리버스 되는것은 아님!
        list_file.delete(index)

# 저장 경로 (폴더를 선택)
def browse_dest_path():
    folder_selceted = filedialog.askdirectory()
    if folder_selceted == '' : #사용자가 취소를 누를 때
        # is None 으로 하면 찾아보기 다시한 후 취소하면 원래 있던 경로도 사라져
        return
        
    # print(folder_selceted) 경로 선택 잘됫나 확인
    txt_dest_path.delete(0, END) #만약 txt_dest..이 entry가 아니라 text형식이었다면
    #(1.0,END로 적어야 된다는 점)
    txt_dest_path.insert(0, folder_selceted)

# 이미지 통합
def merge_image():
    # print("가로넓이 : ", cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포맷 : ", cmb_format.get())
    # 밑에서 관련코드 보이길래 복붙시켜놓은거

    try:
        # 가로넓이
        img_width = cmb_width.get()
        if img_width =="원본유지":
            img_width = -1 #-1은 내가 나중에 쓸려고 정한 값
        else:
            img_width = int(img_width) #1024등의 옵션은 문자열이었거든

        # 간격
        img_space = cmb_space.get()
        if img_space =="좁게":
            img_space = 30
        elif img_space =="보통":
            img_space = 60
        elif img_space =="넓게":
            img_space = 90 
        else: #없음
            img_space = 0
        
        # 포맷
        img_format = cmb_format.get().lower() #PNG, JPG, BMP 값을 받아와서 소문자로 변경

        #############################################################

        images = [Image.open(x) for x in list_file.get(0,END)]

        # 이미지 사이즈 리스트에 넣어서 하나씩 처리(이미지 크기 선택 옵션과정)
        image_sizes=[] # (width1, height1), (width2, height2)...
        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]

        # 계산식
        # 100 * 60 이미지가 있음. width를 80으로 줄이면 height 는?
        # 100 : 60 = 80 : ?

        else :
            # 원본 사이즈 사용
            image_sizes = [(x.size[0], x.size[1]) for x in images]


        
        
        # Image에서 size -> size[0] :width, size[1] : height을 가짐
        # widths=[x.size[0] for x in images]
        # heights = [x.size[1] for x in images]
        # 원래 이 위에 두줄 코드 하면 되는데 zip을 응용해보자
        widths, heights = zip(*(image_sizes))

        # 이미지들 중 최대 넓이와 전체 높이 구해옴
        max_width, total_height = max(widths), sum(heights)
        

        


        # 스케치북 준비
        if img_space > 0: # 이미지 간격 옵션 적용
            total_height += (img_space * (len(images) -1))

        result_img = Image.new("RGB", (max_width, total_height), (255,255,255))
        y_offset = 0 # y좌표의 위치를 다뤄주는 거지
        # for img in images :
        #     result_img.paste(img,(0,y_offset)) # x,y의 값
        #     y_offset += img.size[1] #height 값 만큼 더해줌
        # 밑에꺼 만들면서 같이 처리해줘서 주석처리 하는거임
        
        # 프로그레스바 연동
        for idx, img in enumerate(images): #images를 순회하면서 인덱스와 이미지를 가져온다
            # width가 원본이 아닐 때에는 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img,(0,y_offset)) 
            y_offset += (img.size[1] + img_space) #height 값 + 사용자가 지정한 간격
            
            progress = (idx + 1) / len(images) * 100 #실제 퍼센트 정보 계산, 0을 더하는 이유는 인덱스가 0부터 시작
            p_var.set(progress)
            progress_bar.update()


        # 포맷 옵션 처리
        file_name = "nado_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name) #확장자 씌운거
        result_img.save(dest_path) #이 이미지를 경로에다가 저장해준다잇
        msgbox.showinfo("알림", "작업이 완료되었습니다.")

    except Exception as err: #예외처리
        msgbox.showerror("에러", err)

        
# 시작
def start():
    # 각 옵션들 값을 확인
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() ==0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return # 이 함수를 빠져나가도록 한다..

    # 저장 경로 확인
    if len(txt_dest_path.get()) ==0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    # 이미지 통합 작업
    merge_image()


#파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # x방향으로 쫙~!! 충분히 넓은 공간 차지

btn_add_file=Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file=Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

#리스트 프레임 (리스트박스와 스크롤바의 매핑)
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", 
height=15, yscrollcommand = scrollbar.set)
list_file.pack(side="left",fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임 
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame) #한줄이니까 그냥 엔트리 사용
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) #높이변경의 효과 inner pad..

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이",width=8)
lbl_width.pack(side="left", padx=5, pady=5)

#가로넓이 콤보
opt_width=["원본유지", "1024", "800","640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0) #첫번째 값을 자동으로 선택
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격",width=8)
lbl_space.pack(side="left", padx=5, pady=5)
# 간격 옵션 콤보
opt_space=["없음", "좁게", "보통","넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0) #첫번째 값을 자동으로 선택
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
# 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷",width=8)
lbl_format.pack(side="left", padx=5, pady=5)
# 파일 포맷 옵션 콤보
opt_format=["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0) #첫번째 값을 자동으로 선택
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 프로그래스 바
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress,maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)



root.resizable(False,False)
root.mainloop() 

