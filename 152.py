import os
newfolder=input("새로 생성할 디렉토리 이름을 입력하세요: ")
try:
	os.mkdir(newfolder)
	print("[%s] 디렉토리를 새로 생성했습니다."%newfolder)
except:
	print(e)