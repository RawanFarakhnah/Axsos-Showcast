import random
#Functions Intermediate I
def random_int(min=None,max=None):
    if (min is None and max is None ):
        return random.randrange(0, 1000)
    elif (min is None and not(max is None)):
        return random.randrange(0, max)
    elif (not(min is None) and max is None):
        if min < 100:
           return random.randrange(min, 100)
        else:
            print("Min Vlaue Should less than 100")
    else:
        if min < max:
           return random.randrange(100, 700)
        else:
            print("Min Vlaue Should less than Max Vlaue")
        

print("Random Integer")
print(random_int())
print(random_int(max=3000))
print(random_int(min= -100))
print(random_int(min= 200))
print(random_int(min= 200,max=700))
print(random_int(min= 400,max=50))
