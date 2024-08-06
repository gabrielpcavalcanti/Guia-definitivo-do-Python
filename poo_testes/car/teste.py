from car import EletricCar

# my_new_car = Car('Audi', 'a4', 2016)

# print(my_new_car.get_discriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

my_tesla = EletricCar('Tesla', 'model s', 2016)

print(my_tesla.get_discriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()