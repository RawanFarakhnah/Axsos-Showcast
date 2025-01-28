class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
       self.result -= num
       for n in nums:
           self.result -= n
       return self
    
#Creat an instant of MathDojo
##Note: Without new MathDojo insance (mathDojo3) the results not correct!!

#TEST 1
mathDojo1 = MathDojo()
test1 = mathDojo1.add(2).add(2,5,1).subtract(3,2).result
print("TEST 1 result: ", test1) # output : 5

#TEST 2
mathDojo2 = MathDojo()
test2 = mathDojo2.add(2,5,10).subtract(1,1).result
print("TEST 2 result: ", test2) # output : 15

#TEST 3
mathDojo3 = MathDojo()
test3 = mathDojo3.subtract(2,5,10).result
print("TEST 3 result: ", test3) # output : -17
