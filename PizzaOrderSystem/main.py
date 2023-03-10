import pizza as pz
import sauce as sc
import topping as tp
import drink as dr
import csv
import datetime

Pizzas = {

    1 : pz.ClassicPizza,
    2 : pz.MargheritaPizza,
    3 : pz.TurkPizza,
    4 : pz.PlainPizza
     
}


Toppings = {

    11 : tp.Olives,
    12 : tp.Mushrooms,
    13 : tp.GoatCheese,
    14 : tp.Meat,
    15 : tp.Onions,
    16 : tp.Corn

}


Sauces = {

    21 : sc.Ketchup,
    22 : sc.Mayonnaise,
    23 : sc.Mustard,
    24 : sc.Sriracha,
    25 : sc.BBQ
}

Drinks = {

    31: dr.Coke,
    32: dr.Fanta,
    33: dr.Sprite,
    34: dr.Ayran,
    35: dr.Water
}

########################################################################################

def show_menu():
    # Read the menu from the file
    with open("Menu.txt", "r") as menu_file:
        menu = menu_file.read()
    print(menu)


def get_selection(selection_question, menu, min, max, cancel_character="!", is_multiple_enabled=True, finish_character=0):
    choices=[]
    finish_statement = f", {finish_character} for finishing choice" if is_multiple_enabled else ""
    input_question = f"{selection_question} (Use {cancel_character} to cancel order{finish_statement}..)\n{menu}\n:"
    while True:
        choice = input(input_question)
        if choice == cancel_character:
            return None
        try:
            choice = int(choice)
        except:
            print("You have made an incorrect selection. Please enter a number in the selection range you see on the screen.")
            continue
        
        if choice < min or choice > max:
            if is_multiple_enabled and choice == finish_character:
                return choices
            print("You have made an incorrect selection. Please enter a number in the selection range you see on the screen.")

        else:
            if is_multiple_enabled:
                choices.append(choice)
            else:
                return choice
            



def base_pizza_selection():
    selection_question = "Please choose a pizza choice"
    menu               = """[PIZZAS]
1: Classic---------------₺129.90
2: Margherita------------₺139.90
3: TurkPizza-------------₺45
4: PlainPizza------------₺129.90""" 
    min = 1
    max = 4

    selection = get_selection(selection_question,menu,min,max,is_multiple_enabled=False)
    if selection == None:
        return None
    return Pizzas[selection]()


def add_topping_to_pizza(pizza):
    selection_question = "Please choose a pizza topping"
    menu               = """[TOPPINGS]
11: Olives---------------₺3
12: Mushrooms------------₺5
13: GoatCheese-----------₺10
14: Meat-----------------₺15
15: Onions---------------₺3
16: Corn-----------------₺4""" 
    min = 11
    max = 16

    selections = get_selection(selection_question,menu,min,max)
    if selections == None:
        return None
    for selection in selections:
        pizza.add_topping(Toppings[selection]())
    return pizza
        

def add_sauce_to_pizza(pizza):
    selection_question = "Please choose a pizza sauce"
    menu               = """[SAUCES]
21: Ketchup--------------₺3
22: Mayonnaise-----------₺3
23: Mustard--------------₺3
24: Sriracha-------------₺3
25: BBQ------------------₺3      
"""
    min = 21
    max = 25

    selections = get_selection(selection_question,menu,min,max)
    if selections == None:
        return None
    for selection in selections:
        pizza.add_sauce(Sauces[selection]())
    return pizza

def add_drink_to_pizza(pizza):
    selection_question = "Please choose a pizza drink"
    menu               = """[DRINKS]
31: Coke-----------------₺20
32: Fanta----------------₺20
33: Sprite---------------₺20
34: Ayran----------------₺14
35: Water----------------₺10
"""
    min = 31
    max = 35

    selections = get_selection(selection_question,menu,min,max)
    if selections == None:
        return None
    for selection in selections:
        pizza.add_drink(Drinks[selection]())
    return pizza

def print_order_confirmation(name, pizza):
    # Print the order confirmation to the user
    print(f"Thank you for your order, {name} !")
    print(f"""You ordered the pizza: {pizza.get_description_for_display()}""")
    print(f"Your total cost is ₺{pizza.get_cost()}")
    print("Your order has been recorded in our database.")

def handle_order(pizza_choice):
    
    #Display the cost for the order
    print("Selected pizza: {}".format(pizza_choice.get_description_for_display()))
    print("Total cost: ₺{:.2f}".format(pizza_choice.get_cost()))


    # Prompt the user for payment information
    name = input("Please enter your name: ")
    
    # This loop prompts the user to enter an 11-digit ID number and continues to ask for input until a valid ID number is entered.
    while True:
        id_number = input("Please enter your ID number (11 digits): ")
        if len(id_number) != 11 or not id_number.isdigit():
            print("Invalid input! ID number should contain exactly 11 digits and contain only digits.")
        else:
            break
        
    # This loop will continue until a valid credit card number is entered.
    while True:
        credit_card_number = input("Please enter your credit card number (in the format XXXX-XXXX-XXXX-XXXX): ")
        if not credit_card_number.replace("-", "").isdigit() or len(credit_card_number) != 19:
            print("Invalid input! Credit card number should be in the format XXXX-XXXX-XXXX-XXXX and contain only digits.")
        else:
            break
    # This loop will continue until a valid credit card password is entered.        
    while True:
        credit_card_password = input("Please enter your credit card password (in the format XXXX : ")
        if not credit_card_password.isdigit() or len(credit_card_password) != 4:
            print("Invalid input! Credit card password should be in the format XXXX and contain only digits.")
        else:
            break

    # Get the current date and time
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Write the order to the database file
    with open("Orders_Database.csv", "a",encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            name,
            id_number,
            pizza_choice.get_description(),
            pizza_choice.get_cost(),
            credit_card_number,
            credit_card_password,
            date_time
        ])
    print_order_confirmation(name, pizza_choice)


def main():
    #Show the menu
    show_menu()

    # Get the pizza choice
    pizza_choice = base_pizza_selection()
    if pizza_choice is None:
        return

    pizza_choice = add_topping_to_pizza(pizza_choice)
    if pizza_choice is None:
        return
    
    # Get the sauce choices
    pizza_choice = add_sauce_to_pizza(pizza_choice)
    if pizza_choice is None:
        return
    
    
    pizza_choice = add_drink_to_pizza(pizza_choice)
    if pizza_choice is None:
        return

    # Handle the order
    handle_order(pizza_choice)

if __name__ == "__main__":
    main()


