class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):   # double to that of normal discount
    def get_discount(self):
        return super().get_discount() * 2


class SuperVIPDiscount(Discount):   # four times to that of normal discount
    def get_discount(self):
        return super().get_discount() * 4
