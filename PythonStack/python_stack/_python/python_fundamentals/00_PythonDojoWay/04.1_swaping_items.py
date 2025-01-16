#Imgin fruities is a pointer on three boxes
#Each Box has an address number

fruities =  ["banana" , "apple" , "microsoft"]
print(fruities)

temp = fruities[0]
fruities[0] = fruities[2]
fruities[2] = temp

print(fruities)

#short cut 
fruities[0] , fruities[2] = fruities[2] , fruities[1]
print(fruities)
