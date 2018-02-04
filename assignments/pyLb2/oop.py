
import re

class Person:
    mode=("hapy","tired","lazy");
    def __init__(self,name,money):
        self.name=name;
        self.money=money;
        
        

    def __healthRate(self,healthRate):
        if(healthRate<0 or healthRate>100):
            print("health rate must be between 0 to 100");
        else:
            self.healthRate=healthRate;
             




    def sleep(hours):
        if(hours==7):
            print(self.mode[0]);
        elif(hours>7):
            print(self.mode[1]); 

        elif(hours<7):
            print(self.mode[2]);       

       
    def eat(meals):
        if(meals==3):
            self.healthrate="100% hth";

        elif meals==2:
           self.healtRate="75%"

        elif meals==1:
           self.healtRate="50%"  
           
    
    
    def buy(items):
        self.money -=(items*10);



class Employee (Person):
    
    def __init__(self,name,money,healthrate,id,car,distanceToWork):
        Person.__init__(self,name,money);
        
        self.id=id;
        self.car=car;
        self.distanceToWork=distanceToWork;

    def __salary(self,salay):
        if(salary<1000):
             print("Error salary must be 1000 or more.");
        else:
             self.salary=salary;    

    def __email(self,email):
        EMAIL_REGEX = re.compile(r"\b[\w|\.|-]+@([\w]+\.)+\w{2,4}\b");
        if not EMAIL_REGEX.match(email):
            print("invalled email");
        else:
             self.email=email;    

       
        

             
         
        

    def work(hours):

        if(hours==8):

            print(self.mode[0]);
        elif(hours<8):
            print(self.mode[2]); 

        elif(hours>8):
            print(self.mode[1]);


    def drive(distance):
        
        self.distanceToWork=distance;
        self.velocity=distance/time;
        self.car.run(distance,self.velocity);




    def refue(gasAmount = 100):
        car.fuelRate +=gasAmount;
    def send_mail(to, subject, msg, receiver_name):
        pass                     





class Office:
    def __init__(self,name, employees):
        self.name=name;
        self.employees=employees;
             
    
    def get_all_employees():
        pass
       
    def get_employee():
        pass

    def hire():
        pass

    def fire():
        pass
    def calculate_lateness():
        pass
    def deduct():
        pass
    def reward():
        pass


class Car:
    def __init__(self,name="none"):
        self.name=name;
        
        
    def __velocity(self, velocity): 
        
        if(velocity>0 or velocity<200):
            self.velocity=velocity;
        else:
            print("velocity must be between 0 to 200"); 


    def __fuelRate(self,fuelRate):

        if(fuelRate<0 or fuelRate>100):
            self.fuelRate=fuelRate;
        else:
            print("fuelRate must be between 0 to 100.")    



    def stop(self,remaindis):
        self.velocity -=2;
        if velocity<0:
            if(remaindis==0):
                print("that you arrive the destintation");
            if(remaindis>0):
                print("remain distance = ",remaindis);    
        
        
    def run(self,velocity, distance):
        self.fuelRate -=1;
        self.velocity=velocity;
        self.stop(distance);     



    
e= Employee("yhguj",1000,60,1,Car("h76"),100);
print(e.car.name);
c=Car("56")
c.velocity=20;                     
print(c.velocity);