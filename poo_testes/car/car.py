"""Uma classe que pode ser usado para representar um carro. à gasolina e elétricos."""

class Car:
    """ Uma tentativa simples de representar um carro."""
    
    def __init__(self, make: str, model: str, year: int):
        
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    
    def get_discriptive_name(self) -> str:
        """Devolve um nome descritivo, formatado de modo elegante."""

        #long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        #return long_name

        long_name = [str(self.year), self.make, self.model]
        return " ".join(long_name)
    

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""

        print(f"This car has {self.odometer_reading} miles on it")

    
    def update_odometer(self, mileage: int):
        """Define um valor de leitura do hodômetro com o valor especificado.
        Rejeita a alteração se for tentativa de definir um valor menor para o hodômetro."""

        if mileage >= self.odometer_reading:

            self.odometer_reading = mileage
        
        else:

            print("You can't roll back on odometer!")
    

    def increment_odometer(self, miles: int):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""

        self.odometer_reading += miles 
    

class Battery:
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""

    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size
    

    def describe_battery(self):
        """Exibe uma frase que descreve a capaciade da bateria"""

        print(f"This car has a battery {self.battery_size}-kWh battery")
    

    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria."""

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = f"This car can go approximately {range}"
        message += " miles in a full range."

        print(message)
    
    def upgrade_battery(self):

        self.battery_size = 85

# my_new_car = Car('Audi', 'a4', 2016)
# my_used_car = Car('Subaru', 'Outback', 2014)

# print(my_used_car.get_discriptive_name())

# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
        
class EletricCar(Car):
    """Representa aspectos de um carro específico de veículos elétricos."""

    def __init__(self, make: str, model: str, year: int):
        """Inicializa os atributos da classe-pai."""
        super().__init__(make, model, year)

        self.battery = Battery()
    

my_tesla = EletricCar('Tesla', 'model s', 2016)

# print(my_tesla.get_discriptive_name())

# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

if __name__ == "__main__": 
    my_tesla.battery.get_range()
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.get_range()
