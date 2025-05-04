from suica import Suica
from juice import Vending_machine
from buy import Buy

def main():

    suica = Suica()

    vending_machine = Vending_machine()
    buyer = Buy(vending_machine,suica, 'ペプシ')

    print("--- 購入前 ---")
    vending_machine.show_inventory()
    suica.show_depo()

    buyer.receive("ペプシ", 150)

    print("--- 購入後 ---")
    vending_machine.show_inventory()
    suica.show_depo()

    print("--- 補充前 ---")
    vending_machine.show_inventory()
    vending_machine.get_able_drinks()
    print(vending_machine.restock("ペプシ", 3))

    print("--- 補充後 ---")
    vending_machine.show_inventory()

if __name__ == "__main__":
    main()