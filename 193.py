import socket

HOST=''#host의 값으로 빈 문자열을 지정하면 서버의 컴퓨터 IP를 자동 할당한다.
PORT=9009

def runServer():
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
		sock.bind((HOST,PORT))
		sock.listen(1)#서버가 한 번에 처리가능한 연결 수. 5까지 가능.
		print("클라이언트 연결을 기다리는 중..")
		conn,addr=sock.accept() # accept는 클라이언트로부터 연결요청이 올 때 까지 기다린다. 요청이 오면 TCP소켓과 클라리언트 주소를 리턴한다.
		with conn:
			print("[%s]와 연결됨"%addr[0])
			while True:
				data=conn.recv(1024)#클라이언트로부터 1024바이트를 수신.
				if not data:
					break
				print("메세지 수신[%s]"%data.decode())
				conn.sendall(data)
runServer()