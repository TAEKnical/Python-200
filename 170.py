from urllib.request import urlopen
url = "https://www.python.org"
with urlopen(url) as f:
	doc = f.read().decode() #read는 데이터를 바이트스트림으로 읽어오므로 텍스트인 HTML코드는 decode 해주어야 한다. 96번 참조.
	print(doc)