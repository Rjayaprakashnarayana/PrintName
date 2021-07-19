from abc import ABC, abstractmethod

#Abstract Class
class Bank(ABC):
   def bank_info(self):
       print("Welcome to bank")
   @abstractmethod
   def interest(self):
       "Abstarct Method"
       pass
#Sub class/ child class of abstract class
class SBI(Bank):

   def interest(self):
       "Implementation of abstract method"
       print("In sbi bank 5 rupees interest")

s= SBI()
s.bank_info ()
s.interest()