class Topping:
    def __init__(self, name, cost) -> None:
        self._name = name
        self._cost = cost

    def get_name(self):
        return self._name
    
    def get_cost(self):
        return self._cost
    
################################################################################

class Olives(Topping):
    def __init__(self):
        super().__init__("Olives", 3)

class Mushrooms(Topping):
    def __init__(self):
        super().__init__("Mushrooms", 5)

class GoatCheese(Topping):
    def __init__(self):
        super().__init__("Goat Cheese", 10)

class Meat(Topping):
    def __init__(self):
        super().__init__("Meat", 15)

class Onions(Topping):
    def __init__(self):
        super().__init__("Onions", 3)

class Corn(Topping):
    def __init__(self):
        super().__init__("Corn", 4)

