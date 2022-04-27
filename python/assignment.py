#printing variable
import cmath
from re import T, X


website = "www.gmail.com"
print(website)

#integer devision
num1= 90
num2 = 4.6
quotient = num1//num2
#does not give int after .
print(quotient)
quotient1=num1/num2
#provide int after . 
print(quotient1)

#meters to kilo meters
meter = 90
km =meter/1000
print("{} kilometers".format(km))
# here {} takes up the value of km and format(km) denotes km

#Area of triangle
b= 30
h = 70
area = (b*h)/2
print("Area: {}".format(area))


#Celsius to Fahrenheit
c = 9.3
f = c*1.8+32
print("Fahrenheit: %.2f" %f)

#swaping two numbers
x = 69
y = 44
x,y = y,x
print("a:{} b:{}".format(x,y))

#exponential numbers
b=6
p=7
exp=b**p
print("exponintial:{}".format(exp))

#to solve quadratic equation
x1=1
y1=5
z1=9
#calculating the discriminant
w= (y1**2)-(4*x1*z1)
#finding two solutions
sol1 = (-y-cmath.sqrt(w))/(2*x1)
sol2 = (-y+cmath.sqrt(w))/(2*x1)
print('The solution are {0} and {1}'.format(sol1,sol2))













