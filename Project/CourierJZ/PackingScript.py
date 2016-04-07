# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 12:36:29 2016

@author: dlabadmin
"""

#import array truck that has trucks that have arrays of thier dimensions
pack1 = ["identity1",5,10,15] #w, b and h
pack2 = ["identity2",2,4,6]
pack3 = ["identity3",3,6,9]
#define naximum for lwb from truck database
truckWidth=100;
truckHeight=100;
truckBreadth =100;
truck = [truckWidth,truckHeight,truckBreadth];

Packages= [pack1, pack2,pack3]; #pack 1,2,3, 4 are the package ids
#assuming we have a database of all the packages in the store house
sizeOfPackages=len (Packages);

totalWidth = 0;
totalBreadth = 0;
totalHeight =0;

#calculate how dimensions so that we have the right truck combination

for i in range(1,sizeOfPackages):
     totalWidth = totalWidth + ((Packages[i])[1])
     totalBreadth = totalBreadth +((Packages[i])[2])
     totalHeight = totalHeight + ((Packages[i])[3])
     
print (totalWidth)
print (totalHeight)
print (totalBreadth)

#now that we know the total length,w and breasth , we need to cmpute the total number of trucks
NumOfTrucks = 1;



PackagedHeight =0;
PackagedWidth =0;
PackagedBreadth = 0;
    
condition1 = (truckWidth>=totalWidth)
condition2= (truckHeight>=totalHeight)
condtion3 = (truckBreadth>=totalBreadth)

print(condition1)
print(condition2)
print (condtion3)

allConditions = (condition1 and condition2 and condtion3)

if (allConditions):
    print ("only need one truck")
    
    

while (not allConditions):
    itemsInTruck =[];
    
    PackagedHeight =0;
    PackagedWidth =0;
    PackagedBreadth = 0;
    i=0;

    if (PackagedHeight< truckHeight):
        itemsInTruck.append(Packages[i]);
        PackagedWidth = PackagedWidth + ((Packages[i])[1])
        PackagedBreadth =  PackagedBreadth + ((Packages[i])[2])
        PackagedHeight =  PackagedHeight + ((Packages[i])[3])
        
    
    

    

#while (condition1 or condition2 or condtion3):
#NumOfTrucks = NumOfTrucks+1 ;
