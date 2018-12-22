names = {"Mary":10999,"Sams":2111, "Aimy":9778, "Tom":2024,"Michale":27115,"Bob":5887,"Kelly":7855}
ks=names.keys()
print(ks)

for k in ks:
	print("Key:%s \tValue:%d"%(k,names[k]))