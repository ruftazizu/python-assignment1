def Equalto11(number1): 
    if (11==number1):
        return True
    else:
        return False
print(Equalto11(12))



def Equalto11(number1): 
    if (11==number1):
        return True
    elif (number1 != 11):
        return False
print(Equalto11(11))

def trafficlights(color):
    if ("green"==color):
        print("go")
    elif ("yellow"==color):
        print("wait")
    elif ("red"==color):
        print("stop")

trafficlights("blue")









def studentsgrades(grades):
    if ("A"== grades):
        print("Outstanding") #or return "outstanding"
    elif("B"== grades):
        print("Excellent")
    if ("C"== grades):
        print("Very Good")
    elif("D"== grades):
        print("Good")

print