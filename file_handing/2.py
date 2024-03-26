import os
dir_list = os.listdir()

for dir in dir_list:
    print(dir)
    print(os.path.isfile(dir))
    print(os.path.isdir(dir))
    print("-------")