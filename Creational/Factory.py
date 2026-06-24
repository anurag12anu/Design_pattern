from abc import ABC , abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI_payment(Payment):
    def pay(self):
        print("upi payment has successfull")
class Cart_payment(Payment):
    def pay(self):
        print("cart payment hass successfull")
class Net_banking(Payment):
    def pay(self):
        print("netbanking payment hass successfull ")

class Factory:
    def factory(self,type):
        if type=='upi':
            return UPI_payment()
        elif type=='cart':
            return Cart_payment()
        elif type=='netbanking':
            return Net_banking()
        else:
            return f"invaild payment method"
ob=Factory()
ob.factory('upi')
ob.factory('upi')