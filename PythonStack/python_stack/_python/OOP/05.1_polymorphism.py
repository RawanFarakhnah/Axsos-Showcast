#Overriding & Polymorphism

class Parent:
    def method_a(self):
        print("invoking PARENT method_a")
    
    def pay_bill(self):#function with abstract level
        raise NotImplementedError

class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a")


class Person:
     def pay_bill(self):#function with abstract level
        raise NotImplementedError
    
class Millionaire(Person):
     def pay_bill(self):#function with abstract level
       print("Her you go!! keep the change!")

       
dad = Parent()
dad.method_a()

son = Child()
son.method_a() #override the PARENT method!