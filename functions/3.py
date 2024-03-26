w = [1,2,2,1]
d = 0; da =0
w1 = list(reversed(w))
print(w, ' || ', w1)
for x in range(len(w)):
    if(w[x] == w1[x]):
        da +=1
    else:
        d +=1
if(d > 0): print('no')
else:print('yes')