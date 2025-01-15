#Python Arithmetic Operators
print(5 + 5) #addition output: 10
print(5 - 5) #subtraction output: 0
print(5 * 5) #multiplication output: 25
print(5 / 5) #division output: 1.0
print(5 // 5) #floor division output: 1
print(5 % 5) #modulus output: 0

#exponentiation output: 3125 
#same as #same as 5*5*5*5*5 = 3125
print(5 ** 5) 

#Python Assignment Operators
x = 5 #assign value 5 to variable x
x += 3 #add 3 to x
x -= 3 #subtract 3 from x
x *= 3 #multiply x by 3
x /= 3 #divide x by 3
x %= 3 #modulus x by 3  
x //= 3 #floor division x by 3
x **= 3 #exponentiation, the same as x*x*x

#using &= operator (bitwise AND) "Convert the numbers to binary"
#The AND (&) operator results in 1 only if both bits are 1
x = 5 
x &= 3 #output: 1

#using |= operator (bitwise OR)
#The OR (|) operator results in 1 if any of the bits is 1
x = 5
x |= 3 #output: 7

#using ^= operator (bitwise XOR)
#The XOR (^) operator results in 1 only if the bits are different
x = 5
x ^= 3 #output: 6

#using >>= operator (right shift)
#The right shift (>>) operator moves the bits to the right
x = 5 # represents 101 in binary (8-bit representation) 0000 0101
x >>= 3 #output : 0 after shifting 3 bits to the right 0000 0000

#using <<= operator (left shift)
#The left shift (<<) operator moves the bits to the left
x = 5 # represents 101 in binary (8-bit representation) 0000 0101
x <<= 3 # shiftting 3 bits to left 0000 0101 << 0010 1000 = 40

#using := operator (walrus operator)
#The walrus operator assigns values to variables as part of an expression
x = 5
print(x := 10) #output: 10 , evaluates to 10

#Python Comparison Operators
#Comparison operators are used to compare two values
print(x > 0) #Greater than
print(x < 0) #Less than
print(x >= 0) #Greater than or Equal
print(x <= 0) #Less than or Equal
print(x == 5) #Equal
print(x != 5) #Not Equal

#Python Logical Operators
#Logical operators are used to combine conditional statements

#using and operator
#returns True if both statements are true
num = 5
print (num > 0 and num < 10) #output: True

#using or operator
#returns True if one of statements are true
print (num < 0 or num < 10) #output: True

#using not operator
#reverse the result, returns False if the result is true

#Python Identity Operators
