from restaurant import Restaurant, IceCreamStand








restaurant = Restaurant('Pushkin', 'Russian cuisine')
restaurant.describe_restaurant()

icecreamstand = IceCreamStand('Pattison', 'italian', flavors=['vanilla', 'chocolate', 'strawberry', 'pistachio'])
print(f"В нашем ресторане представлены вкусы: {icecreamstand.get_flavors_string()}")

#flavors_line = icecreamstand.get_flavors_string()
#icecreamstand.save_report_to_file('flavors.txt', f"Our flavors today: {flavors_line}.")