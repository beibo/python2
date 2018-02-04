
def calcArea(ch,n1,n2=1):
    ch.lower()
    area=0;
    if(ch is "t"):
        area=0.5*n1*n2;
        return area;
    elif(ch is "r" ):
        area=(n2*n1*2);
        return area;
    elif (ch is "c"):

        area=(22/7)*n1;
        return area;
    else:
        return"your char not corect plez enter anthor one";   
          




# l=input("enter [t] or [r] or [c] :",)
# print(l);

# a=0;    

# if(l is "c"):

    
#     numb1=int(input("enter frist number: "))
#     a=calcArea(l,numb1);
#     print("area of circle : ",a )

# elif(l is "r" or l is "t"):
#     numb1=int(input("enter frist number: "))
#     numb2=int(input("enter second number: "))
    
#     a=calcArea(l,numb2,numb2) 
#     print("area of",l,"=",a)  

  

print(calcArea("r",4,2))




