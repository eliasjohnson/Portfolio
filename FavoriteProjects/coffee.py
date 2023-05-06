"""
"I declare that the following source code was written solely by me.
 I understand that copying any source code, in whole or in part, constitutes 
cheating, and that I will receive a zero on this project if I am 
found in violation of this policy."

Project 4: Coffee Machine
@Author: Elias Johnson
Class: CS 1410
Date: 10/31/2021
"""


class CoffeeMachine:
    '''responsible for constructing machine, capturing external input.'''
    def __init__(self):
      self.__cashBox = CashBox()
      self.__selector = Selector(self.__cashBox)


    def oneAction(self):
      '''requests user input and prints the instructions'''
      print("""
______________________________________
    PRODUCT LIST: all 35 cents, except bouillon (25 cents)
    1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouilon"
    Sample commands: insert 25, select 1.""")
      user_command = input(">>> Your command: ").lower()
      user_command_parts = user_command.split()
      if user_command_parts[0] == 'insert':
        self.__cashBox.deposit(int(user_command_parts[1]))
        return True
      elif user_command_parts[0] == 'cancel':
        self.__cashBox.returnCoins()
      elif user_command_parts[0] == 'select':
        self.__selector.select(int(user_command_parts[1]))
        return True
      elif user_command_parts[0] == 'quit':
        self.__cashBox.returnCoins()
        return False
      else:
        print("Invalid command.")
        return True

    def totalCash(self):
      return self.__cashBox.total()


class CashBox:
  '''Responsible for accepting and tracking coins, making change.'''
  def __init__(self):
    self.__credit = 0
    self.__totalReceived = 0

  def deposit(self, amount):
    if amount not in (5, 10, 25, 50):
      print("INPUT ERROR >>>")
      print("We only take half-dollars, quarters, dimes, and nickels.")
      print("Coin(s) returned.")
    else:
      self.__credit += amount
      print(f"Depositing {amount} cents. You have {self.__credit} cents credit.")

  def returnCoins(self):
    if self.__credit > 0:
      print(f"Returning {self.__credit} cents.")
      self.__credit = 0

  def haveYou(self, amount):
    return self.__credit >= amount

  def deduct(self, amount):
    if (amount > self.__credit):
      raise ValueError("Insufficient credit")
    else:
      self.__credit -= amount
      self.__totalReceived += amount

  def total(self):
    return self.__totalReceived


class Selector:
  '''Knows products and selection coordinates payment and drink making.'''
  def __init__(self, cashbox):
    self.__cashBox = cashbox
    self.__products = [None, Product('black', 35, ['cup', 'coffee', 'water']), Product('white', 35, ['cup', 'coffee', 'creamer', 'water']),\
       Product('sweet', 35, ['cup', 'coffee', 'sugar', 'water']), Product('white & sweet', 35, ['cup', 'coffee', 'sugar', 'creamer', 'water']),\
          Product('bouillon', 25, ['cup', 'bouillonPowder', 'water'])]

  def select(self, choiceIndex):
    if choiceIndex < 1 or choiceIndex >= len(self.__products):
      print("Invalid selection.")
      return
    product = self.__products[choiceIndex]
    if not self.__cashBox.haveYou(product.getPrice()):
      print("Sorry. Not enough money deposited.")
      return
    self.__cashBox.deduct(product.getPrice())
    product.make()
    self.__cashBox.returnCoins()


class Product:
  ''''Responsible for knowing its price and recipe, also dispenses the drink.'''
  def __init__(self, name, price, recipe):
    self.__name = name
    self.__price = price
    self.__recipe = recipe

  def getPrice(self):
    return self.__price

  def make(self):
    print(f"Making {self.__name}...")
    for ingredient in self.__recipe:
      print(f"      Dispensing {ingredient}")


def main():
  '''the main program that makes an object (m) and runs oneAction in a while loop. then prints total.'''
  m = CoffeeMachine()
  while m.oneAction():
    pass
  total = m.totalCash()
  print(f"Total cash: ${total/100:.2f}")


if __name__ == '__main__': # conditional statement that runs main if it exists
  main()
