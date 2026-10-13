
def make_pizza(size, *toppings):
    """Выводит описание пиццы"""
    print(f"\nMaking a {size}-cm pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        