#convert miles to kilometers
def miles_to_kilometers(miles):
    kilometers = miles * 1.60934;
    return "{0} miles equal {1} kilometers \n".format(miles , kilometers)


kmVal1 = miles_to_kilometers(20)
print(kmVal1)

kmVal2 = miles_to_kilometers(40)
print(kmVal2)