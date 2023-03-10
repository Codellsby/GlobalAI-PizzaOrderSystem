class Sauce:
    def __init__(self,name,cost) -> None:
        self._name = name
        self._cost = cost


    def get_name(self):
        return self._name
    

    def get_cost(self):
        return self._cost
    

#########################################################


class Ketchup(Sauce):
    def __init__(self) -> None:
        super().__init__("Ketchup", 3)

class Mayonnaise(Sauce):
    def __init__(self) -> None:
        super().__init__("Mayonnaise", 3)

class Mustard(Sauce):
    def __init__(self) -> None:
        super().__init__("Mustard", 3)

class Sriracha(Sauce):
    def __init__(self) -> None:
        super().__init__("Sriracha",4)

class BBQ(Sauce):
    def __init__(self) -> None:
        super().__init__("BBQ", 3)

