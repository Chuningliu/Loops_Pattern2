# 1
# 2 3 4
# 5 6 7 8 9

i=1
s=0
while i<4:
    j=1
    while j<i+i:
        print(s+1, end=" ")
        s+=1
        j+=1
    print()
    i+=1
    