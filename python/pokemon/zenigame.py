from pokemon import Pokemon
class Zenigame(Pokemon):
    def _zenigame_attack(self):
        return f"{self.name}のみずてっぽう！"

    def _zenigame_type(self):
        return f"{self.name}は{self.type1}{self.type2}タイプです"

    def _zenigame_hp(self):
        return f"{self.name}はHPが{self.hp}です"

    def show_zenigame(self):
        print(self._zenigame_attack())
        print(self._zenigame_type())
        print(self._zenigame_hp())