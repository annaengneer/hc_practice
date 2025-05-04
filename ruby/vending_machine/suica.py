class Suica:
# デフォルトで500円チャージされていて
    def __init__(self):
        self._balance = 500

    def get_balance(self):
        return self._balance

    def deposit(self, add_depo):
        # 100円以上の任意の数字をチャージできる
        if add_depo >= 100:
            self._balance += add_depo
        else:
            # 100円未満をチャージしようとした場合は例外を発生
            print('100円未満はチャージできません')

    def pay(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            raise Exception('残高不足です')

    def show_depo(self):
        print(self._balance)
    
# 残高を取得できる
mysuica = Suica()
mysuica.deposit(2000)
mysuica.show_depo()