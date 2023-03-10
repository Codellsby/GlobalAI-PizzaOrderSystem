class Drink:
    def __init__(self,name,cost) -> None:
        self._name = name
        self._cost = cost

    def get_name(self):
        return self._name
    

    def get_cost(self):
        return self._cost

#######################################################

class Coke(Drink):
    def __init__(self) -> None:
        super().__init__("Coke", 20)

class Fanta(Drink):
    def __init__(self) -> None:
        super().__init__("Fanta", 20)

class Sprite(Drink):
    def __init__(self) -> None:
        super().__init__("Sprite", 20)

class Ayran(Drink):
    def __init__(self) -> None:
        super().__init__("Ayran", 14)

class Water(Drink):
    def __init__(self) -> None:
        super().__init__("Water", 10)