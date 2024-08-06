class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str):

        self.restaurante_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    

    def describe_restaurant(self):

        print(f"Nome do resturante: {self.restaurante_name}")
        print(f"Tipo de cozinha: {self.cuisine_type}")
        print(f"Clientes atendidos: {self.number_served}")
    
    
    def open_restaurant(self):
        
        print("O restaurante está aberto.")
    

    def set_number_served(self, number_client: int):

        self.number_served = number_client
    

    def increment_number_served(self, clients: int):

        self.number_served += clients


class IceCreamStand(Restaurant):

#res1 = Restaurant("Outback", "Stack house and bar")
    def __init__(self, restaurant_name: str, cuisine_type: str, flavors: list[str]):
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = flavors
    
    def show_flavors(self):
        """Mostra os sabores de sorvete que a sorveteria possui."""

        for i in self.flavors:
            print(i)


sorveteria01 = IceCreamStand("sorveteria do Gabriel", "sorvete", ["Chocolate", "morango", "creme", "flocos"])\

sorveteria01.show_flavors()
    