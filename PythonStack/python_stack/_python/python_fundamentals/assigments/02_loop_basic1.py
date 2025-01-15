#01 Basic - Print all integers from 0 to 150.
for i in range(150+1):
    print(i)


#02 Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5 , 1000):
    if i % 5:
        print(i)

#03 Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1,100):
     if i % 5 == 0:
        print(i , "Coding")
     if i % 10 == 0:
        print(i , "Coding Dojo")

#04 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for i in range(500000):
    if i % 2 != 0:
        sum += i
print(sum)

#05 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    print(i)

#06 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
lowNum, highNum, mult = 2, 9 , 3
for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)