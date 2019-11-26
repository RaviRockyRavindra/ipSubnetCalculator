#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Sun Nov 24 11:07:25 2019

@author: Ravindra Sai Konna


"""

import itertools
import time as hytg


from prettytable import PrettyTable as ptablerockyconcantrowsandcolumns


t = ptablerockyconcantrowsandcolumns(['Ip', 'Subnet' , 'Class ', 'Public Ip', 'Private Ip','Network Bits','Host Bits','Apipa','Loop Back'])



t2 = ptablerockyconcantrowsandcolumns(['1st Octect ','2nd Octect','3rd Octect','4th Octect'])

t3= ptablerockyconcantrowsandcolumns(['Available Ips'])

def available_ip_list(input_ip,subnet):
    
    full_subnets = 32
    
    available_ips=full_subnets-subnet
    
    ip_count=pow(2,available_ips)
    
    split_input_here=input_ip.split(".")
    
    splitting_ip=[int(i) for i in split_input_here]
    
    print(splitting_ip)
    
    finallist=[]
    
    finallist.append(splitting_ip)
    
    t3.add_row([ip_count-2])
    
    for tt in range(5):
        
        hytg.sleep(1)
        print("\t *")
    
    print(t3)
    
    #print(finallist)    
        
        
        


def subnet_process(subnet,input_ip):
    
    networkbits=[]
    
    for o in range(subnet):
        
        networkbits+="1"
    
    hostbits=32-subnet
    
    for u in range(hostbits):
        
        networkbits+="0"
    
    pos=0
    
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    
    for h in networkbits:
        
        pos=pos+1
        
        if pos<=8:
        
           list1+=h
           
        elif (pos>=9) and (pos<=16):
            
            list2+=h
            
        elif (pos>=17) and (pos<=24):
            
            list3+=h
            
        elif (pos>=25) and (pos<=32):
            
            list4+=h    
    
    
    t2.add_row([list1,list2,list3,list4])
    
    print(t2)
    
    
    available_ip_list(input_ip,subnet)
    
    
    
    
    
    


        
    
    
    
                

def ip_class_process(octect,input_ip,input_subnet):
    
    try:
        
        Public='Y'
        private='N'
        loopback='N'
        Apipa='N'
        classs=' '
    
        if octect <= 126:
            
           classs='A'   
            
        elif (octect >= 128) and (octect <= 191):
            
            classs='B'
        
        elif (octect >= 192) and (octect <= 223):
            
            classs='C'
            
        elif (octect >= 224) and (octect <= 239):
            
            classs='D'  
            
        elif (octect >= 240) and (octect <= 255):
            
            classs='E' 
            
        
        split_input_ippp=input_ip.split(".")
        
        print(split_input_ippp)
        
        split_input_ip=[int(i) for i in split_input_ippp]
        
        if (split_input_ip[0]==10):
            
            private='Y'
            Public='N'
            
        elif (split_input_ip[0]==127):
            
             loopback='Y'
             Public='N'
             private='N'
             
        elif (split_input_ip[0]==169) and (split_input_ip[1]>=254):
            
             Apipa='Y'
             Public='N'
             private='N'
            
        elif (split_input_ip[0]==172) and ((split_input_ip[1]>=16) and (split_input_ip[1]<=31)):
        
              private='Y'
              Public= 'N'
            
        elif (split_input_ip[0]==192) and  ((split_input_ip[1]>=168)):  
        
             private='Y'
             Public='N'


        total_subnet=32
        
        hbits= total_subnet-int(input_subnet)
        
        
        
        nbits= input_subnet
        
        t.add_row([input_ip , input_subnet , classs , Public ,private , nbits , hbits, Apipa,loopback])    
            
        print(t)
        
        for q in range(5):
                
                hytg.sleep(1)
                print("\t *")
                
        
        
        
            
            
        
        
    
    
    except KeyboardInterrupt:
        
          print("Interrupted by the User, exiting\n")
    
    except ValueError:
        
            print("Seem to have entered an incorrect value, exiting\n")  
        
        

def Ip_process():
    
    try:

        targetaddress=input("Enter your ip address ...  ex:0.0.0.0/0..? ")
        
        ip_subnet_splitting=targetaddress.split("/")
        
        input_ip=ip_subnet_splitting[0]
        
        input_subnet=ip_subnet_splitting[1]

        splittingg_ip=input_ip.split(".")
    
        splitting_ip=[int(i) for i in splittingg_ip]
    
        if (len(splitting_ip)==4) and (splitting_ip[0]!=0) and (splitting_ip[0]<=255) and (splitting_ip[1]<=255) and (splitting_ip[2]<=255) and (splitting_ip[3]<=254) and ((splitting_ip[3]!=255) and (splitting_ip[0]!=169) and (int(input_subnet)<=32)):
            
            
            for q in range(5):
                
                hytg.sleep(1)
                print("\t *")
            
            print("\t ***  Validating the Input Ip Address ***")
            
            for w in range(5):
                
                hytg.sleep(1)
                print("\t *")
            
            print("\t ***  Validating the SubnetBits ***")
            
            for e in range(5):
                
                hytg.sleep(1)
                print("\t *")
            
    
            ip_class_process(splitting_ip[0],input_ip,input_subnet)
            
            
            subnet_process(int(input_subnet),input_ip)
            
                
                
        
        
        else:
        
            print("\n  "+targetaddress + "  ---- is invaild try again with valid Ip address and subnetbits ")
        
    

    except Exception as ew: print(ew)         
       
        
if __name__ == '__main__':
   Ip_process()

