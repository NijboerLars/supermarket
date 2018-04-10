from product import *
from register import *

register = Register()

p1 = Product('washing powder', 3)
p1.get_selling_price()
p2 = Product('butter', 3)
p2.get_selling_price()
p3 = Product('chocolate', 2)
p3.get_selling_price()

products = [p1,p2,p3]

register.add_products(products)
register.get_total_price()
register.request_payment()
register.print_receipt()
