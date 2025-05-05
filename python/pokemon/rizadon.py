from pokemon import Pokemon

class Rizadon(Pokemon):
    def _rizadon_attack(self):
        return f"{self.name}のかえんほうしゃ!"

    def _rizadon_type(self):
        return (f"{self.name}は{self.type1}と{self.type2}タイプです")

    def _rizadon_hp(self):
        return f"{self.name}はHPが{self.hp}です"

    def show_rizadon(self):
        print(self._rizadon_attack())
        print(self._rizadon_type())
        print(self._rizadon_hp())