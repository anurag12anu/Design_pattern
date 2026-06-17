from abc import ABC, abstractmethod

class PaymentProccessor(ABC):
    @abstractmethod
    def pay(self):
        pass
class RazorpayGetway:
    def make_payment(self,amount):
        return f"paid ${amount} using razorpay"
class RazorpayAdopter(PaymentProccessor):
    
        def __init__(self,razorpay):
            self.razorpay=razorpay
            
        def pay(self,amount):
            return self.razorpay.make_payment(amount)


getway=RazorpayGetway()
payment=RazorpayAdopter(getway)
print(payment.pay(500))