class Pub:
    def __init__(self, name, till, selection_of_drinks):
        self.name = name
        self.till = till
        self.selection_of_drinks = selection_of_drinks

    def drinks_list(self):
        return len(self.selection_of_drinks)

    def increase_till(self, amount):
        self.till += amount

    def find_drink_by_name(self, drink_choice):
        for drink in self.selection_of_drinks:
            if drink.name == drink_choice:
                return drink

    def sell_drink_to_customer(self, drink_choice, customer):
        customers_drink = self.find_drink_by_name(drink_choice)
        customer.reduce_wallet(customers_drink.price)
        self.increase_till(customers_drink.price)