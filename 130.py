names = {"Mary":10999,"Sams":2111, "Aimy":9778, "Tom":2024,"Michale":27115,"Bob":5887,"Kelly":7855}
k = input("이름을 입력하세요:")
if k in names:
	print("이름이 <%s>인 출생아 수는 <%d> 명입니다."%(k,names[k]))
else:
	print("자료에 이름이 <%s>인 출새아는 없습니다.")