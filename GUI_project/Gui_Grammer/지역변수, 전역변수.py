# def hi():
#     a=3
#     return a, 3, "hi"

# print(hi())
# ######################################
# def hi():
#     a=3
#     return a

# def bye():
#     if hi()==3:
#         print("이게 return의 사용법인가")

# bye()
######################################
def hi():
    for i in range(1,100):
        print(i)
    a=3
    ㅠ=4
    return a, ㅠ

def bye():
    if hi()==(3,4):
        print("이게 return의 사용법인가")

bye() #자 여기서 보면 if안에 hi있는거 있잖아.. 거기서 hi()반환값을 따오는게 아니라 작동시키는 개념이네 끝처리로 반환이고..
######################################

        