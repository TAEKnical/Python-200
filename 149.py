from os import rename

target_file="stockcode.txt"
newpath=input("[%s]를 이동할 디렉터리의 절대경로를 입력하세요:"%target_file)

if newpath[-1] == '\\':
	newname=newpath+target_file
else:
	newname=newpath+'\\'+target_file
try:
	rename(target_file,newname)#파일을 다른 디렉토리로 이동하려면 rename에 이동할 디렉터리 경로를 같이 넘겨준다.
	print("[%s]->[%s]로 이동되었습니다."%(target_file,newname))
except FileNotFoundError as e:
	print(e)