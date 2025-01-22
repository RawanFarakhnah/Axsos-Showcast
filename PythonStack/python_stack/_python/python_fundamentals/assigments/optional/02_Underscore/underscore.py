#Underscore Assignment

class Underscore:
    def map(self, iterable, callback):
        new_iterable = list()
        for item in iterable:
            new_item = callback(item)
            new_iterable.append(new_item)
        return new_iterable

    def find(self, iterable, callback):
       for item in iterable:
           if callback(item) == True:
               return item

    def filter(self, iterable, callback):
        new_iterable = list()
        for item in iterable:
           if callback(item) == True:
              new_iterable.append(item)
        return new_iterable
    
    def reject(self, iterable, callback):
        new_iterable = list()
        for item in iterable:
           if callback(item) == False:
              new_iterable.append(item)
        return new_iterable

_ = Underscore()

print("\nUsing Custome Map")
double = _.map([1,2,3,4,5,6], lambda x: x * 2)
print("double", double)

print("\nUsing Custome Filter")
evens = _.filter([1,2,3,4,5,6], lambda x: x % 2 == 0)
print("evens", evens)

print("\nUsing Custome Find Method")
match_item = _.find([1,2,3,4,5,6], lambda x: x > 4)
print("first item found", match_item)

print("\nUsing Custome Reject Method")
reject = _.reject([1,2,3,4,5,6], lambda x: x % 2 == 0)
print(reject)

