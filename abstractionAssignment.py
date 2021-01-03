from abc import ABC, abstractmethod

class car(ABC):
    #parent class using the Abstract Base Class module
    def paySlip(self, amount):
        print("Your purchase amount:", amount)
    @abstractmethod #labeling as an abstract method
    def payment(self, amount):
        print("Processing payment...")

class DebitCardPayment(car):
    #child class of car
     def payment(self, amount):
        super().payment(amount) #calls the abstract payment method
        print("Your purchase amount of {} exceeded your $100 limit".format(amount))

obj = DebitCardPayment() #creating the object
obj.paySlip("$400")
obj.payment("$400")
