class PreciousStone:
    def __init__(self, carats=0.0, price=0.0, name="Unknown"):
        self.__carats = carats
        self.__price = price
        self.__name = name

        self.public_number_field = 0
        self.public_string_field = "Default"

    def get_carats(self):
        return self.__carats
    
    def set_carats(self, carats):
        self.__carats = carats

    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"PreciousStone(name={self.__name}, carats={self.__carats}, price={self.__price})"
    
    def __repr__(self):
        return f"PreciousStone({self.__name}, {self.__carats}, {self.__price})"

    def __del__(self):
        print(f"PreciousStone {self.__name} is being deleted")

def main():
    stone1 = PreciousStone(1.5, 5000, "Diamond")
    stone2 = PreciousStone(2.0, 10000, "Ruby")
    stone3 = PreciousStone(0.8, 2000, "Sapphire")

    for stone in [stone1, stone2, stone3]:
        print(stone)
        print("Public Number Field:", stone.public_number_field)
        print("Public String Field:", stone.public_string_field)
        print()

if __name__ == "__main__":
    main()
