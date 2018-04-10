from product import *
from math import floor
import datetime

class Discount:

    def __init__(self):
        self.discount_value = 0

    def calculate_discount(product_name, product_number):
        discount_value = 0
        if product_name.lower() == 'washing powder' and product_number >= 2:
            if (product_number % 2) == 0:
                discount_value = product_number * 8.00 * 0.30
            else:
                discount_value = (product_number-1) * 8.00 * 0.30
        if product_name.lower() == 'yoghurt' and datetime.datetime.now().isoweekday() == 3:
            discount_value = 0.50 * product_number
        if product_name.lower() == 'butter':
            discount_value = floor(product_number / 4) * 2.25
        return discount_value
