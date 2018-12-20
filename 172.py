from urllib.request import urlopen

imgurl = "http://img.insight.co.kr/static/2017/12/22/700/uq625rnu1u3wz3510qta.jpg"
imgname = imgurl.split("/")[-1]
try:
	with urlopen(imgurl) as f:
		with open(imgname,'wb') as h:
			img = f.read()
			h.write(img)
except Exception as e:
	print(e)