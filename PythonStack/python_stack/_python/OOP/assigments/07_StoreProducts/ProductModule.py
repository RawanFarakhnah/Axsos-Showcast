class Product:
    _counter = 0 #class variable 

    def __init__(self, name, price, category):
        self.id = Product._counter #instance variabel 
        Product._counter += 1
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change
        else:
          self.price -= self.price * percent_change
        return self
    
    def __str__(self):
        return f"{self.id} {self.name} ({self.category}): ${self.price:.2f}"

    def print_info(self):
        message = "Product ID: {0}, Name: {1}, Category: {2}, Price: {3:.2f}".format(self.id, self.name, self.category, self.price)
        return message

print(__name__)

if __name__ == "__main__":
  product1 = Product("Laptop", 1200.99, "Electronics")
  print(product1.print_info())
  product1.update_price(0.02, True)
  print(product1.print_info())
  product1.update_price(0.02, False)
  print(product1.print_info())

  product2 = Product("Laptop2", 1400.99, "Electronics")
  print("\n" + product2.print_info())

