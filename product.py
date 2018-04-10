from discount import *

class Product:

    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.base_price = 0
        self.discount_value = 0
        self.selling_price = 0

    def get_selling_price(self):
        if self.name.lower() == 'washing powder':
            self.base_price = 8.00
        if self.name.lower() == 'chocolate':
            self.base_price = 2.00
        if self.name.lower() == 'chinese vegetables':
            self.base_price = 3.00
        if self.name.lower() == 'yoghurt':
            self.base_price = 1.50
        if self.name.lower() == 'butter':
            self.base_price = 2.25
        self.discount_value = Discount.calculate_discount(self.name, self.number)
        self.selling_price = self.base_price * self.number - self.discount_value
        return self.selling_price

    def __str__(self):
        return self.name + self.selling_price
