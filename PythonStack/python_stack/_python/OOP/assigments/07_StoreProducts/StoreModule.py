from ProductModule import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = [] 

    def __str__(self):
        message = ""
        if self.products:
           for product in self.products:
               message += product.print_info() + "\n"

        return f"{self.name}({len(self.products)})\n{message}"
    

    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                return self
            
        print("Product Id Not Found")
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self
    
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category.lower() == category.lower():
                product.update_price(percent_discount, False)
        return self
    
if __name__ == "__main__":
    #initalize store and its products
    my_store = Store("Sama Mobile")
    products_list = [
        Product("Laptop", 1200.99, "Electronics"),
        Product("Phone", 699.99, "Electronics"),
        Product("Tablet", 299.99,  "Electronics"),
        Product("Puzzle", 12.99,  "Toys")
    ]
    
    #set product to our store
    for product in products_list:
        my_store.add_product(product)

    print("#1 Store Initalization")
    print(my_store)

    print("#2 Sell Product")
    my_store.sell_product(1)
    print(my_store)

    print("#3 After Inflation")
    my_store.inflation(0.02)
    print(my_store)

    print("#4 After Toys Clearance")
    my_store.set_clearance("Toys", 0.01)
    print(my_store)
    