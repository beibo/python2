def characterlocator(str,letter):
    listindex=[];
    for i in range(len(str)):
        if letter is str[i]:
            listindex.append(i)
                   
    return listindex 



#str=input("enter your word:") 
#l=input("your number you want letter: ");

#t=characterlocator("mohamed","m");
#print(t);



