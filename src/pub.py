class Pub:
    def __init__(self, name, till, selection_of_drinks):
        self.name = name
        self.till = till
        self.selection_of_drinks = selection_of_drinks

    def stock_count(self):
        return len(self.selection_of_drinks)