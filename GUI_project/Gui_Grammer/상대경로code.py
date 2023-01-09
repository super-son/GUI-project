import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

## 현재경로와 상대경로를 합쳐서 절대경로로 변경주는것
## 이걸 쓴다고 해서 찐 절대경로가 되는건 아니야. 그럼에도 이걸 쓰는이유는
## pyinstaller에서 -F속성을 이용해서 하나로 합칠때 빛을 바란다. 찐 절대경로에 -F를 써도 이미지 못 찾네
## 압축된 exe 파일을 실행시키면 임시경로에 압축을하는데 거기서 실행을 시키고 끝나면 삭제시키는데
## 임시폴더의 이름이 매번바뀌기 때문에 절대경로를 잡아주는 역할을 하지
## 그럼 -F를 쓰고싶다면 이 절대경로코드를 사용해주고 pyinstaller 속성에는
## --add-data 'src;dest' src:추가할파일 dest:어느위치(실행파일과 같은 경로라면 그냥 .적으면된다)
## EX) --add-data '.gui_basic\*.png;gui_basic'
## 최종 입력 : pyinstaller -w --add-data '.\3_images\*.png;3_images' -F .\3_label.py 하 개 같은거
 photo = PhotoImage(file=r"3_images\check.png")   #얘를 이렇게 변형
 photo = PhotoImage(file=resource_path(r"3_images\check.png")) 


 ######################################################### pygame에선 이런게 있었지.
# current_path = os.path.dirname(__file__) #현재 파일의 위치 반환 # 상대 경로로 받아오는 개 꿀팁
# image_path = os.path.join(current_path, "images") # 이미지 폴더 위치 변환

# #배경만들기
# background = pygame.image.load(os.path.join(image_path, "background.png"))