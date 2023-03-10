# Pizza Üst Sınıfı Oluşturma
def _format_items(items):
    item_counts = {}
    for item in items:
        if item.get_name() in item_counts:
            item_counts[item.get_name()] += 1
        else:
            item_counts[item.get_name()] = 1
    formatted_items = []
    for item, count in item_counts.items():
        if count > 1:
            formatted_items.append(f"{item} x{count}")
        else:
            formatted_items.append(item)
    return ', '.join(formatted_items) if formatted_items else "" 


class Pizza:
    def __init__(self,name,cost,description) -> None:
        # Örnek değişkenler
        self._name             = name             # Pizza Adı
        self._base_cost        = cost             # Pizza Taban Fiyatı
        self._base_description = description      # Pizza açıklaması
        self._sauces           = []               # Pizzayı eklenen ekstra sosları tutmak için liste
        self._toppings         = []               # Pizzaya eklenen ekstra malzemeleri tutmak için liste
        self._drinks           = []
    

    def get_name(self):
        return self._name                         # Pizza Adını döndür
    

    def get_cost(self):
        total_cost = self._base_cost
        for topping in self._toppings:
            total_cost += topping.get_cost()
        for sauce in self._sauces:
            total_cost += sauce.get_cost()
        for drink in self._drinks:
            total_cost += drink.get_cost()
        
        return total_cost


    def get_description(self):
        _toppings = ', '.join([topping._name for topping in self._toppings]) if self._toppings else 'NaN'
        _sauces = ', '.join([sauce._name for sauce in self._sauces]) if self._sauces else 'NaN'
        _drink =  ', '.join([drink._name for drink in self._drinks]) if self._drinks else 'NaN'
        return f"{self._name}, {_toppings}, {_sauces}, {_drink}."
    
    def get_description_for_display(self):
        toppings = _format_items(self._toppings)
        sauces = _format_items(self._sauces)
        drinks =_format_items(self._drinks)
        description = f"{self._name}"
        if toppings != "":
            description += f"\nToppings: {toppings}"
        if sauces != "":
            description += f"\nSauces: {sauces}"
        if drinks != "":
            description += f"\nDrinks: {drinks}"
        return description
        





    def get_sauces(self):       
        return self._sauces                       # Pizzaya eklenen sosları döndür
    

    def add_sauce(self,sauce):
        self._sauces.append(sauce)                # Verilen sosu soslar listesine ekler

    
    def add_topping(self,topping):
        self._toppings.append(topping)            # Verilen malzemeyi malzeme listesine ekler

    def add_drink(self,drink):
        self._drinks.append(drink)




#################################################################################################


class ClassicPizza(Pizza):
    def __init__(self) -> None:
        super().__init__("Classic Pizza", 129.90, "Mozzarella, Tomato Sauce")
        self._toppings = []

class MargheritaPizza(Pizza):
    def __init__(self) -> None:
        super().__init__("Margherita Pizza", 139.90, "Mozzarella, Tomato Sauce, Basil")

class TurkPizza(Pizza):
    def __init__(self) -> None:
        super().__init__("Turk Pizza", 45, "Ground Beef, Tomato, Onion, Pepper")

class PlainPizza(Pizza):
    def __init__(self) -> None:
        super().__init__("Plain Pizza", 129.90, "Sausage, Mushroom, Olive, Mozzarella, Tomato Sauce")