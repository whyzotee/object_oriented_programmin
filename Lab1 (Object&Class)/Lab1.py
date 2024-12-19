class Player:
    def __init__(self, id, name, level, HP, Weapon=None, Armor=None, guild=None):
        self.id = id
        self.name = name
        self.level = level
        self.HP = HP
        self.Weapon = Weapon
        self.Armor = Armor
        self.guild = guild

    def info(self):
        print(f"=== Player {self.id} ===")
        print("Name: ", self.name)
        print("Level: ", self.level)
        print("HP: ", self.HP)
        print("Weapon: ", self.Weapon.name, end=' ')
        print(f"(Damage: {self.Weapon.dmg})")
        print("Armor: ", self.Armor.name , end=' ')
        print(f"(Amount: {self.Armor.amount})")
        print("Guild:", self.guild.name)
        print()
    
    def death(self):
        self.HP = 0

    def add_guild(self, guild):
        self.guild = guild

class Weapon:
    def __init__(self, name, dmg, magazine, reserve, credits):
        self.name = name
        self.dmg = dmg
        self.magazine = magazine
        self.reserve = reserve
        self.credits = credits
    
    def shoot(self):
        if (self.magazine == 0):
            self.reload()

        self.magazine -= 1
    
    def reload(self):
        if (self.reserve == 0):
            return
        elif (self.reserve > 25):
            self.magazine = 25
            self.reserve -= 25
        else:
            self.magazine = self.reserve

    def animated():
        pass

class Armor:
    def __init__(self, name, amount, credits, regen=False):
        self.name = name
        self.amount = amount
        self.credits = credits
        self.regen = regen
    
    def regen_armor():
        pass

    def take_damage():
        pass
    
    def reset():
        pass

class Guild:
    def __init__(self, name, guild_master):
        self.name = name
        self.member = []
        self.guild_master = guild_master
    
    def add_member(self, player):
        self.member.append(player)

    def remove_member(self, player):
        for i in self.member:
            if i == player.id:
                self.member.remove(i)

    def info(self):
        print(f"=== Guild Name: {self.name} ===")
        print(f"* Guild Master: {self.guild_master.name} *")

        for data in self.member:
            print(f"{data.name}")
        print()

# === Instace Zone === #
gun1 = Weapon("Vandal", 40, 25, 50, 2900)
player1 = Player("U001", "Toast", 239, 100, gun1)
armor1 = Armor("Light", "25", "400")

gun2 = Weapon("Sheriff", 55, 6, 24, 800)
player2 = Player("U002","Nompangping", 123, 100, gun2)
armor2 = Armor("Regen", "25", "650", True)

gun3 = Weapon("Judge", 17, 5, 15, 1850)
player3 = Player("U003", "PumKungZ", 500, 100, gun3)
armor3 = Armor("Heavy", "50", "1000")

guild_mofu = Guild("MofuNetive", guild_master=player1)
guild_oakza = Guild("OakZa", guild_master=player3)

player1.Armor = armor1
player2.Armor = armor2
player3.Armor = armor3

guild_mofu.add_member(player1)
guild_mofu.add_member(player2)
player1.add_guild(guild_mofu)
player2.add_guild(guild_mofu)

guild_oakza.add_member(player3)
player3.add_guild(guild_oakza)

# === Print Zone === #
guild_mofu.info()
guild_oakza.info()
player1.info()
player2.info()
player3.info()