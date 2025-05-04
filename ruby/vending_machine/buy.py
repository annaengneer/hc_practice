from suica import Suica
from juice import Vending_machine

class Buy:

    def __init__(self,vending_machine, suica, juice_name):
        self.vending_machine = vending_machine
        self.suica = suica
        self.juice_name = juice_name
    
    # ジュースを購入
    def receive(self,name,price):
        counter = {}
        for juice in self.vending_machine.get_inventory():
            counter[juice.name] = counter.get(juice.name, 0) + 1
        # 残高がジュースの値段以上ある and ジュースが一本以上ある
        if (self.suica.get_balance() >= price) and (counter.get(self.juice_name, 0) + 1):
            for i, juice in enumerate(self.vending_machine.get_inventory()):
                if juice.name == self.juice_name:
                    # 在庫を1本減らす
                    del self.vending_machine.get_inventory()[i]
                    break
            # 売り上げ金額を増やす
            self.vending_machine._sales += price
            #suicaの残高を減らす
            self.suica.pay(price)
        else:
            # suicaの残高不足か在庫切れはエラー表示
            print("チャージが足りないか在庫がありません")



   

