"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #1 (25 points)
Filename: shoppers.py

An item has an item code (e.g. "ABCD-1234"), a name (e.g. "Silky Camisole"), 
and a price (e.g. $24). 
A partially completed item class has been provided to you below. You must 
complete the class by making the following enhancements:
- Write accessors for all fields.
- Two items are considered equal if they have the same item code.
- Items should be capable of being used with hashing data structures.
- The string representation of an item is its its code, name, and price
  seperated by commmas in a parenthesis, e.g. "(ABCD-1234, Silky Camisole, 24)"
- Items can be sorted based on the item code.
Write down the manual test by creating at least two items.
"""

class Item:
    __slots__ = ["__code", "__name", "__price"]
    
    def __init__(self, code, name, price):
      self.__code = code
      self.__name = name
      self.__price = price
    
    def get_code(self):
      return self.__code
    
    def get_name(self):
      return self.__name
    
    def get_price(self):
      return self.__price
    
    def __eq__(self, other):
      if type(self) == type(other):
        return self.__code == other.__code
      else:
        return False
    
    def __hash__(self):
      return hash(self.__code)
    
    def __repr__(self):
      return "(" + self.__code + ", " + self.__name + ", " + str(self.__price) + ")"
    
    def __lt__(self, other):
      return self.__code < other.__code


# manual test from main() method
def main():
  item1 = Item("ABCD-1234", "Silky Camisole", 24)
  item2 = Item("EFGH-5678", "Grapes", 8)
  item3 = Item("ABCD-1234", "Milk", 12)
  items = [item1, item2]
  dictionary = {}
  for item in items: # hashable test
    key = item.get_code()
    dictionary[key] = item
  code = item1.get_code()
  name = item1.get_name()
  price = item1.get_price()
  print(code, name, price) # accessors test
  print(item1 == item2) # equality tests
  print(item1 == item3)
  print(items) # __repr__ test
  items.sort() # sortable test
  print(items)

if __name__ == "__main__":    main()