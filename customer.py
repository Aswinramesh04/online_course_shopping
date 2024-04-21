class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = []


    def add_to_cart(self, course):
        self.cart.append(course)

    def view_cart(self):
        return self.cart

    def calculate_total_price(self):
        return sum(course.price for course in self.cart) # java, python
