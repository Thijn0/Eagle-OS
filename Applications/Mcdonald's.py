class MenuItem:
  def __init__(self, name, price):
      self.name = name
      self.price = price

class McDonaldsOrder:
  def __init__(self):
      self.menu = [
          MenuItem('Big Mac', 3.99),
          MenuItem('Quarter Pounder', 3.79),
          MenuItem('McChicken', 1.29),
          MenuItem('French Fries', 1.19),
          MenuItem('Cola', 1.00),
          MenuItem('Salade', 2.99)
      ]
      self.order = []

  def display_menu(self):
      print("Dit is ons menu:")
      for idx, item in enumerate(self.menu):
          print(f"{idx + 1}. {item.name} - €{item.price:.2f}")

  def take_order(self):
      while True:
          self.display_menu()
          choice = input("Is er iets wat je graag zou willen? Type dan het nummer van het item in. klaar? Type dan 'klaar': \n").strip()
          if choice.lower() == 'klaar':
              break
          if not choice.isdigit() or not 1 <= int(choice) <= len(self.menu):
              print("Sorry dat leveren we momenteel niet, maar kies gerust een van onze andere opties")
              continue
          item_index = int(choice) - 1
          quantity = input(f"Hoeveel {self.menu[item_index].name}(s) wilt u bestellen? \n").strip()
          if not quantity.isdigit() or int(quantity) <= 0:
              print("Invalid quantity. Please try again.")
              continue
          self.order.append((self.menu[item_index], int(quantity)))
          print(f"{quantity} {self.menu[item_index].name}(s) toegevoegd aan je order.\n")

  def calculate_total(self):
      total = sum(item.price * quantity for item, quantity in self.order)
      return total

  def display_order(self):
      if not self.order:
          print("Je hebt nog niks besteld.")
          return
      print("\nje order is nu:")
      for item, quantity in self.order:
          print(f"{quantity} x {item.name} - €{item.price * quantity:.2f}")
      total = self.calculate_total()
      print(f"\nPrijs: €{total:.2f}")

def main():
  order = McDonaldsOrder()
  order.take_order()
  order.display_order()

if __name__ == "__main__":
  main()