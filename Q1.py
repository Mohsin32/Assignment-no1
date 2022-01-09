import datetime
import platform
from math import pi

                        #Qno1
print("""Twinkle, twinkle,little star,
                  How I wonder what you are!
                          Up above the world so high,
                          Like a daimond in the sky.
Twinkle, twinkle,little star,
         How I wonder what you are!""")
                       #Qno.2
print(platform.python_version());
                       #Qno.3
x=datetime.datetime.now();
print(x);

                      #Qno.4

r = float(input ("Enter radius of circle : "))

print ("Area of the circle is: " + str(pi * r**2))
                     #Qno.5
first=input("Enter your first name : ")
sec=input("Enter your last name : ")
print(sec+"""  """+first)

                    #Qno.6
a=int(input("please enter a number"))
b=int(input("please enter a 2nd number"))
c=a+b
print(a," + ",b," = ",c)