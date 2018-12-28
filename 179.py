#로또 번호 추출기
from random import shuffle
from time import sleep

gamenum=input("로또 게임 횟수를 입력하세요:")
balls=[]
for i in range(int(gamenum)):
	for x in range(45):
		balls.append(x+1)
	ret=[]
	for j in range(6):
		shuffle(balls)
		number = balls.pop()#pop은 리스트의 가장 마지막을 추출 후 제거
		ret.append(number)
	ret.sort()
	print("로또번호[%d]:"%(i+1),end='')
	print(ret)
	sleep(1)
