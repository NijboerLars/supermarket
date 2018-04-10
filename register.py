from product import *
from payment import *

class Register:

    def __init__(self):
        self.products = []
        self.total_price = 0
        self.paid = False

    def add_products(self, products):
        self.products = products

    def get_total_price(self):
        for item in self.products:
            self.total_price += item.selling_price
        #print('The total price is:', self.total_price)
        return self.total_price

    def request_payment(self):
        payment = Payment()
        payment.get_payment()
        self.paid = True
        #print('Payment succeeded.')

    def print_receipt(self):
        print('\nReceipt\n')
        for item in self.products:
            print('Product: %s, Number: %s, Price: %s' % (item.name.capitalize(), item.number, item.selling_price))
        print('Total price:', self.total_price)

    def __str__(self):
        return str(self.products)
