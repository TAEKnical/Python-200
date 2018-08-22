txt = 'aAbBcCdDeEfFgGhHiIjJkK'
ret = txt[::2] # 처음에서 : 끝까지 : 2칸씩 = 홀수번째
ret2 = txt[1::2] #인덱스1에서 : 끝까지 : 2칸씩  =짝수번째
print(ret) #abcdefghijk가 출력됨
print(ret2) #ABCDEFGHIJK가 출력됨
