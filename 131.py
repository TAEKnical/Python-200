names = {"Mary":10999,"Sams":2111, "Aimy":9778, "Tom":2024,"Michale":27115,"Bob":5887,"Kelly":7855}
print(names.items())


ret1 = sorted(names)
print(ret1)

def f1(x):
	return x[0]

def f2(x):
	return x[1]

print(f1(names.items()))
print(f2(names.items()))

ret2 = sorted(names.items(),key=f1) #sotred는 key인자를 이용해서 정렬할 기준이 되는 값을 지정할 수 있다. key의 값은 반드시 함수명. 함수의 처리결과가 정령릐 기준. 첫 번째 인자를 리턴
print(ret2)

ret3 = sorted(names.items(),key=f2) #두번째 인자를 리턴
print(ret3)

ret4 = sorted(names.items(),key=f2,reverse=True)
print(ret4)