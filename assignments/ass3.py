def mulitiTable(num):
    list1=[];
    
    x=1;
    for i in range(1,num+1):
        dd=[];
        for j in range(1,i+1):
            x=j*i;
            dd.append(x);  
        list1.append(dd);
    return list1;
           

#numb=input("enter number you want :")
#print(int(numb));
#n=int(numb)
#ll=mulitiTable(2);
#print(ll)