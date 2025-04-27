class Juice:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
class Vending_machine:
    def __init__(self):
        self._inventory={
            "ペプシ":{"juice":Juice("ペプシ",150),"count":5},
            "モンスター":{"juice":Juice("モンスター",230),"count":5},
            "いろはす":{"juice":Juice("いろはす",120),"count":5}
        }
        self._sales = 0

    def get_inventory(self):
        return self._inventory

    def get_able_drinks(self):
        able = []
        for name, i in self._inventory.items():
            if i["count"] > 0:
                able.append(name)
        return able
    def restock(self, name, number):
        if name in self._inventory:
            self ._inventory[name]["count"] += number
            return f"{name}を{number}本補充しました"
        else:
            return f"{name}は自動販売機にありません"

    def show_inventory(self):
        print(self._inventory)
        
vending_machine = Vending_machine()
vending_machine.show_inventory()
print(vending_machine.get_able_drinks())
vending_machine.restock("ペプシ", 3)
