import os
with open("2.txt", "w") as file:
    file.write("thise was written from 6.py")

file.close()
from time import sleep

for i in range(1, 2):
    sleep(2)

os.remove("2.txt")