txt = "A lot of things occur each day, every day."
offset1 = txt.find("e")
offset2 = txt.find("day")
offset3 = txt.find("day",30)#30은 검색 시작위치
print(offset1)
print(offset2)
print(offset3)