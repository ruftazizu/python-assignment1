#Create a program that reads two integers, **a** and *b*, from the user. Your program should compute and display:
import math
a =input("First number:")
b =input("Second number:")
a =int(a)
b =int(b)

# The sum of **a** and **b.**
sum = a + b
print(sum)

# The difference when **b** is subtracted from *a*

difference = a - b
print(difference)

# The product of **a** and *b*

product = a * b
print(product)

# The quotient when **a** is divided by *b*

divided = a//b
print(divided)

# The remainder when **a** is divided by *b*
remainder = a % b
print(remainder)

# The result of $log_{10}a$
log = math.log10(a)
print(log)

# The result of ab 

exp = a ** b
print(exp)

#In the US, fuel efficiency for vehicles is normally expressed in miles-per-gallon (MPG).
#In Canada, fuel efficiency is normally expressed in liters-per-hundred-kilometers (L/100 km).
#Use your research skills to determine how to convert from MPG to L/100 km. 
#Then create a program that reads a value from the user (in American units) and displays the equivalent fuel efficiency in Canadian units.

user_input_mpg = float(input())
conversion = 235.21/user_input_mpg
print(conversion)

#The surface of the earth is curved, and the distance between degrees of longitude varies with latitude.
#As a result, finding the distance between two points on the surface of the earth is more complicated than simply using the Pythagorean theorem.
#The equation for finding the distance between two points on the surface of the earth in kilometers is given by:
#distance = 6371.01 \times arccos(sin(lat_1) \times sin(lat_2)+cos(lat_1)\times cos(lat_2)\times cos(long_1-long_2))
#where: $(lat_1, long_1)$ and $(lat_2,long_2) $ are the latitude and longitude of two points on the Earth’s surface.
#Create a program that allows the user to enter the latitude and longitude of two points on the Earth in degrees.
#Your program should display the distance between the points in kilometers.
#Also assuming we travel using an aeroplane that is moving at a minimum speed of 740 km/h how long will it take us to travel that distance?

import math

lat_eritrea, long_eritrea = 15.1794, 39.7823

lat_stockholm, long_stockholm = 59.3293, 18.0686

current_country = input("What your current country is: ")
lat1 =float(input("What your current latitude is: "))
long1 = float(input("What your current longtitude is: "))
destination_country = float(input("What your destination country is: "))
lat2 = float(input("What your destination latitude is: "))
long2 = float(input("What your destination longtitude is: "))

pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)

math.radians()

distance = 6371.01 * math.acos(math.sin(lat1)*math.sin(lat2)+math.cos(lat1)*math.cos(lat2)*math.cos(long1-long2))
print(distance)