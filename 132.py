ch = input("문자를 1개 입력하세요 :")
if len(ch)!=0:
	ch = ch[0]#여러 문자가 입력되면 첫문자만
	chv = ord(ch)#아스키 코드값으로 변환
	print("문자:%s\t코드값:%d[%s]"%(ch,chv,hex(chv)))#한글 가 를 입력하면 유니코드값이 출력됨