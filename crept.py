import os
filename = input('input_filename plz: ')
if os.path.isfile(filename) and filename[-3:] == 'exe':
    str = open(filename,'rb').read()
    print(str)
else:
    print("File no found please check!!!")

