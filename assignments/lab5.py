
def dictionary(l):

    l.sort();
    dd={};
    for i in l:

        if i[0] in dd:
            dd[i[0]].append(i);
        else:    
            dd[i[0]]=[i];
    return dd; 


# li=['fggggggggg', 'atma', 'ibrahim'];
# dic=dictionary(li);
# print(dic)


