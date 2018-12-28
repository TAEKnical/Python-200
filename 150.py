import os,glob

folder = "C:\\Users\\hogoo\\Dropbox\\python\\python200"
file_list = os.listdir(folder)
print(file_list)

files='*.txt'
file_list=glob.glob(files)
print(file_list)