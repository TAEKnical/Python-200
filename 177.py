from zipfile import *
import os

def compressAll(zipname,folder):
	print("[%s]->[%s] 압축.."%(folder,zipname))
	with ZipFile(zipname,"w") as ziph:
		for dirname, subdirs, files in os.walk(folder): #walk는 [('tmp',['tmp의서브디렉터리'],['tmp의 찾은 파일들']),('서브1',['서브1의서브디렉토리'],['서브1의 찾은파일틀'])] 순서로 리턴
			for file in files:
				ziph.write(os.path.join(dirname,file))

folder="hello"
zipname=folder+".zip"
compressAll(zipname,folder)