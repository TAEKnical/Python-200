#파일의 특정 부분만 복사하기
spos = 105 #파일을 읽는 위치 지정. 105 바이트부터 읽음.
size = 500 #읽을 크기를 지정

f=open("stockcode.txt", "r")
h=open("stockcode_port.txt","w")

f.seek(spos)
data=f.read(size)
h.write(data)

h.close()
f.close()