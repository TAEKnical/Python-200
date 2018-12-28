#여러개로 분리된 파일을 하나로 합치기
BUFSIZE=256*1024
merge_filename="ret.exe"
filelist=[]
for x in range(10):
	filelist.append("다운로드실습용.exe_"+str(x))

with open(merge_filename,"wb") as f:
	for filename in filelist:
		print("[%s] 합치는 중..." %filename)
		with open(filename, "rb") as h:
			buf = h.read(BUFSIZE)
			while buf:
				f.write(buf)
				buf=h.read(BUFSIZE)
print("파일 합치기가 완료되었습니다.")