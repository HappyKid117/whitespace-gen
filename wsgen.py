s = "TECHWKND{3l3my1}"
for i in s:
    print("   ",end="")
    b=bin(ord(i))
    t=str(b)
    for j in t:
        if(j=='0'):
            print(" ",end="")
        elif(j=='1'):
            print("\t",end="")
    print()
    print("\t")
    print("  ",end="")
print()
print()
print()