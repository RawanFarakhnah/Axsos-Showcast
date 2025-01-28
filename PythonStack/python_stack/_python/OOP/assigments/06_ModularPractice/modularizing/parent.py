local_val = "magical unicorns"

def square(x):
    return x * x

class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return "hello"

print(square(5))
#used to determind if python script being run directly or 
# imported as a module

print(__name__)

if __name__ == "__main__":
    print("the file is being executed directly")
    user = User("Anna")
    print(user.name)
    print(user.say_hello())
else:
    print("the file is being executed becouse it is imported by another file. the file is called:", __name__)