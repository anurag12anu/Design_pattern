   #      Client
    #         |
   #          v
    #    Target Interface
    #         ^
     #        |
     #    Adapter
     #        |
     #        v
     #    Adaptee """


from abc import ABC, abstractmethod


"""1. Target (Expected Interface)

The interface that the client expects."""

class PaymentProccessor(ABC):
    @abstractmethod
    def pay(self):
        pass
    
    
    
"""2. Adaptee (Existing Class)

A third-party class with an incompatible interface.""" 

class RazorpayGetway:
    def make_payment(self,amount):
        return f"paid ${amount} using razorpay"
    
    
"""3. Adapter

Converts the Adaptee interface into the Target interface."""

class RazorpayAdopter(PaymentProccessor):
    
        def __init__(self,razorpay):
            self.razorpay=razorpay
            
        def pay(self,amount):
            return self.razorpay.make_payment(amount)



"""4. Client

Uses the Target interface without knowing about the Adaptee"""

getway=RazorpayGetway()
payment=RazorpayAdopter(getway)
print(payment.pay(500))