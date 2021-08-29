#Declaration of variables
a = 23
b = 12
c = 2.402
name = "Tshepo"
surname = "Gabonamang"
#Basic operations
full_name = name + surname #concatenate strings
sum = a + b 
product = a*b 
sumth = a**b #exponent
bb = b**2
divc = a / b 
subtract = a - b 
divs = a%b 

#Assignment Operators
c += b
d = e = f = g = h = i = 5
d -= 12
e *=0.5
f /= 2
g **= 2
h %= 3
i //= d 

#Comparison Operators
a == b 
b != d 
a < c 
i > d 
a <= 9
b >= b 

#Logical Operators
print(True and True)
print(True or False)
print(True and False)
print(True and not False)
print(True and False)#row 2
print(True or False)
print(True and not False)

#String Operators
var1, var2, var3 = "Tshepo", "Gobonamang", "I love Python"
print(var1 + " " + var2)
print(var3*2)
print(var3[:6] + " " +var1)
print(var2 + " " + var3[2:])
print("lov" in var3)
print("lov" in var2)
print("lov" not in var3)
print("lov" not in var2)

#A code that calculates area of a circle and working with user inputs
var4 = input("Enter the value of the radius :") #input expects a string
carea = 3.142 * int(var4) * 2 # cast that string to an integer
print("The area of this circle is: %d" % (carea))

#Calculating a simple interest
rate, principal_amount, time - 0.03, 28000, 6
si = principal_amount*rate*time
print("The simple interest of %d for %d years at %d percent, is %2.f"%(principal_amount, time, (100*rate),si))
