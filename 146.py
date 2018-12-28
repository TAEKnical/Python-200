from os.path import getsize

file1 = "stockcode.txt"
file2 = "C:/Users/hogoo/Dropbox/python/python200/img_sample.jpg"
file_size1 = getsize(file1)
file_size2 = getsize(file2)

print("File name : %s \tFile Size: %d"%(file1,file_size1))
print("File name : %s \tFile Size: %d"%(file2,file_size2))