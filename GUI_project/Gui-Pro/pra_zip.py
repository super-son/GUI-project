kor = ["사과","바나나","오렌지"]
eng = ["apple","banana","orange"]

print(list(zip(kor, eng)))
#그냥 프린터만 해서 출력안되면 list로 명시해준다
#zip은 저렇게 세로로 리스트목록을 합쳐주는 기능

mixed=[('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]  
print(list(zip(*mixed))) #별을 넣음으로써 분리를 한다는 뜻

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)