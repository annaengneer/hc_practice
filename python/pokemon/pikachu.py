from pokemon import Pokemon
class Pikachu(Pokemon):
    def _pikachu_attack(self):
        return f"{self.name}の10万ボルト！"

    def _pikachu_type(self):
        return f"{self.name}は{self.type1}{self.type2}タイプです"

    def _pikachu_hp(self):
        return f"{self.name}はHPが{self.hp}です"

    def show_pikachu(self):
        print(self._pikachu_attack())
        print(self._pikachu_type())
        print(self._pikachu_hp())
