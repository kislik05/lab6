a = input() 
y = 0; upd = 0; low = 0
for x in range(len(a)):
    for s in range(65, 91):
        if(a[x] == chr(s)):
            upd = upd + 1    
for x in range(len(a)):
    for s in range(97, 122):
        if(a[x] == chr(s)):
            low = low + 1

print('upd: ', upd)
print('low: ', low)