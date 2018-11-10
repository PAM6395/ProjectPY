#python Inter

import os

file_obj = open('test.txt','w+') #us a+ for append
print file_obj.name,"||",file_obj.closed,"||",file_obj.mode

file_obj.write("Test Python File Write!")
file_obj.write("\nLine 2")
file_obj.close()
file_obj = open('test.txt','r+')
out = file_obj.readline()
out = file_obj.readline()
print "test.txt :: ",out

file_obj.close()
print file_obj.name,"||",file_obj.closed,"||",file_obj.mode

folder_list = os.listdir("C:\Python27")

for folder in folder_list:
	if (folder.find(".") == -1):
		print folder
	