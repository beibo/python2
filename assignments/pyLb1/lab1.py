
def removeVowle(w):
    nw="";
    v="aioueAIOUE";
    for i in w:
        if (i in v):
            nw +="";
        else:
            nw +=i;
    return nw
            

#str=removeVowle("reMove");
#print(str);

if __name__=='__main__ ':
    print("hellwo")

