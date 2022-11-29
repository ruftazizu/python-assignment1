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

#Distance units: Create a program that begins by reading a measurement from the user in feet.
#Then your program should display the equivalent distance in inches, yards and miles.
#Use your research skills to look up the necessary conversion factors.

d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)

#Area of a regular polygon: A polygon is regular if its sides are all the same length and the angles between all of the adjacent sides are equal.
#The area of a regular polygon can be computed using the following formula, where s is the length of a side and n is the number of sides.
#Write a program that reads s and n from the user and then displays the area of a regular polygon constructed from these values.

from math import tan, pi
n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)

#Current Time: Python has a couple of modules that can be used when working with time.
#This includes a module called time and a function/method within the time module called asctime. 
#It reads the current time from the computer’s internal clock and returns it in a human-readable format. 
#Write a program that displays the current time and date. Your program will not require any input from the user.

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#Wind Chill Index: When the wind blows in cold weather, the air feels even colder that it actually is because the movement of the air increases the rate of cooling for warm objects, like people.
#This effect is known as wind chill.
#The formula below is used to compute the wind chill index.
#Where: $T_a$ is the air temperature in degrees Celsius and $V$ is the wind speed in kilometers per hour.
#Write a program that begins by reading the air temperature and wind speed from the user. 
#Once these values have been read, your program should display the wind chill index rounded to the closes integer.

import math
v = float(input("Input wind speed in kilometers/hour: "))
t = float(input("Input air temperature in degrees Celsius: "))
wci = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
print("The wind chill index is", int(round(wci, 0)))

#Sum of digits in an integer: Develop a program that reads a four digit integer from the user and displays the sum of the digits in the number. 
#For example, if the user enters 3141 then your program should display the result of the sum $3+1+4+1=9$.

num = int(input("Input a four digit number: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is: ", x+x1+x2+x3)