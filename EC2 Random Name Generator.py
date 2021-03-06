#!usr/bin/env/ python3.7

#Python Implemention here

# Week 15 project: Random EC2 Generator

# Create a unique name generator function

import random 
import string
def string_generator(size=8, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))
    
    #Allow the user to input how many EC2 instances they want names for and output the same amount of unique names.

number = int(input("Enter number of EC2 instances with a unique name:"))

Signature = input("Enter signature here: ")

Department = input("Choose name of desired department: Security_Ops, Business_Ops, or Network_Ops: ")

for _ in Department:
    
    if Department == "Security_Ops" :
        print("Security_Ops")
        break
    
    elif Department == "Business_Ops" :
        print("Business_Ops")
        break
    
    elif Department == "Network_Ops" :
        print("Network_Ops")
        break
    
    else:
        print("Error: You can not access this generator")
        exit()
    
#Generate random characters and numbers that will be included in the unique name.

for _ in range(1, number + 1):
    unique_name = Signature + Department
    EC2_identity = unique_name + "_" + string_generator()
    print("Your EC2's unique name is : ", EC2_identity)
    
    
    
    
    
    


