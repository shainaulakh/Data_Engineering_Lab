class SaleTransaction:
    def __init__(self, customer_id, product, price, quantity, shipping_city):
        self.customer_id = customer_id
        self.product = product
        self.price = float(price)
        self.quantity = int(quantity)
        self.shipping_city = shipping_city.strip().title()

    def total(self):
        return self.price * self.quantity


def parse_coupon(code):
    if code == 'SAVE10':
        return 0.10
    elif code == 'WELCOME20':
        return 0.20
    return 0.00
