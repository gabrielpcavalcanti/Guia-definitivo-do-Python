class Item:

   all = []

   def __init__(self, name: str, price: float, quantity: int):

      self.name = name
      self.price = price
      self.quantity = quantity

      # Actions to execute
      Item.all.append(self)
    

   @staticmethod
   def is_numeric(num):
        if isinstance(num, float):
            print("It is numeric")
        elif isinstance(num, int):
            print("It is numeric")
        else:
            print("It is not numeric")
 

Item.is_numeric(3)
Item.is_numeric("oi")

