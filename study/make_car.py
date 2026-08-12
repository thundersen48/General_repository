#8.14. Автомобили.

def make_car(manufacturer, model_name, **car_data):
    car_data['manufacturer'] = manufacturer
    car_data['model_name'] = model_name

    print(f"\nИнформация о {car_data.get('manufacturer')} {car_data.get('model_name')}")
    return car_data
   