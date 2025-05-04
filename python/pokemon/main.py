from rizadon import Rizadon
from pikachu import Pikachu
from zenigame import Zenigame

def main():

    pikachu = Pikachu("ピカチュウ","でんき","","40")
    zenigame = Zenigame("ゼニガメ","みず","","30")
    rizadon = Rizadon("リザードン", "ほのお","ひこう",300)

    pikachu.show_pikachu()
    zenigame.show_zenigame()
    rizadon.show_rizadon()

if __name__ == "__main__":
    main()