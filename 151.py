import os
pdir = os.getcwd()#현재 디렉토리 가져옴
print(pdir) #현재 디렉토리 확인
os.chdir('..')#상위 디렉토리 이동
print(os.getcwd())# 상위 디렉토리 확인
os.chdir(pdir)#다시 최초 디렉토리로 이동
print(os.getcwd())