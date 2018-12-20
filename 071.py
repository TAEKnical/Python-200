def getPrime(n):
	if n%2 == 0:
		return
	for i in range(3,int(n/2),2):
		if n%i ==0:
			break
	else:
		return n

listdata = [117,119,1113,11113,11119]
ret = filter(getPrime,listdata)
print(list(ret))