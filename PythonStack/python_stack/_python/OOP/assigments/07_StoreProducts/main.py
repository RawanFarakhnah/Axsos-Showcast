from StoreModule import Store
from ProductModule import Product

class Main:
    def __init__(self, stor_name, products_list=[]):
        #initalize store and its products
        self.store = Store(stor_name)
        self.products = products_list

        if len(products_list) > 0:
           self.set_store_products()
        
    def set_store_products(self):
        #set product to our store
        for product in self.products:
            self.store.add_product(product)
    
    def display_store(self):
        print(self.store)


if __name__ == "__main__":
   products_list = [
        Product("Laptop", 1200.99, "Electronics"),
        Product("Phone", 699.99, "Electronics"),
        Product("Tablet", 299.99,  "Electronics"),
        Product("Puzzle", 12.99,  "Toys")
    ]
   
   main = Main("Shein" , products_list )
   main.display_store()