import random
#Functions Intermediate I
def random_int(min=0,max=1000):
    if max > min :
        return random.randrange(min,max)
    else:
        raise ValueError("Max must be begger than Min")

print("Random Integer")
print(random_int())
print(random_int(max=3000))
print(random_int(min= -100))
print(random_int(min= 200))
print(random_int(min= 200,max=700))
print(random_int(min= 400,max=50))
