import time
s = [0.1, 0.3, 0.5, 0.7, 1, 1.2]
for i in range(len(s)):
    time.sleep(s[i])
    print(s)