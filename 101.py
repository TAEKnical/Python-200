solarsys=["태양","수성","금성","지구","화성","목성","토성","천왕성","해왕성","지구"]
planet="지구"
pos=solarsys.index(planet)+1
print("%s은(는) 리스트에서 %d번째에 위치하고 있습니다."%(planet,pos))
pos=solarsys.index(planet,5)+1 #5번째 이부후터 검색. 앞은 신경 안씀.
print("%s은(는) 리스트에서 %d번째에 위치하고 있습니다."%(planet,pos))