from collections import Counter
class Juice:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
class Vending_machine:
    def __init__(self):
        self._inventory=[]
        self._sales = 0
        self._initalize_inventory()

    def _initalize_inventory(self):
        for _ in range(5):
            self._inventory.append(Juice("ペプシ", 150))
        for _ in range(5):
            self._inventory.append(Juice("モンスター", 230))
        for _ in range(5):
            self._inventory.append(Juice("いろはす", 120))

    def get_inventory(self):
        return self._inventory

    def get_able_drinks(self):
        names = [juice.name for juice in self._inventory]
        return Counter(names)
       
    def restock(self, name, number):
        price = None
        for juice in self._inventory:
            if juice.name == name:
                price =juice.price
                break
        if price is None:
            return f"{name}は自動販売機にありません"

        for _ in range(number):
            self._inventory.append(Juice(name, price))
        return f"{name}を{number}本補充しました"
            

    def show_inventory(self):
        count = {}
        for juice in self._inventory:
                count[juice.name] = count.get(juice.name, 0) + 1

        for name, number in count.items():
            print(f"{name}:{number}本")

