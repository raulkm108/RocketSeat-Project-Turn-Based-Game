class Character:
    def __init__(self, name, hp, lvl):
        self.__name = name
        self.__hp = hp
        self.__lvl = lvl

    def get_name(self):
        return self.__name
    
    def get_hp(self):
        return self.__hp
    
    def get_lvl(self):
        return self.__lvl