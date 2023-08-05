import os
os.chdir('C:\\Users\\USER\\Desktop\\')
file_path = "新增 Text Document.txt"
if os.path.isfile(file_path):
    print('檔案存在')
else:
    print('不存在')
