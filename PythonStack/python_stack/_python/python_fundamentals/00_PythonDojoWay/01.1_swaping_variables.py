
#Swaping Variables
var1 = "first string"
var2 = "second string"

print(f"var1 {var1}")
print(f"var2 {var2}")

temp = var1
var1 = var2
var2 = temp

print("\nafter swaping")
print(f"var1 {var1}")
print(f"var2 {var2}")