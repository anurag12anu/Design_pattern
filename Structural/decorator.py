 #        Component
#            ^
 #             |
  #    ----------------
  #    |              |
# Concrete      Decorator
# Component         ^
 #                 |
  #        Concrete Decorator """"
  
  
from abc import ABC, abstractmethod

# Component
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 100

# Decorator Base
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

# Concrete Decorator
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 20

# Concrete Decorator
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 30


coffee = SimpleCoffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)

print(coffee.cost())