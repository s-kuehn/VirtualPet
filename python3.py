import math
import random

class Player():
    def __init__(self):
        self.inventory = {}

    def useItem(self):
        # Print player inventory and use items
        if self.inventory == {}:
            print("\nInventory is empty..")
        else:
            print("\nWhat item would you like to use? \n \nID | ITEM | AMOUNT")
            countItems = 0
            for item in self.inventory:
                countItems += 1
                print(f'{str(countItems)}. {str(item)} : {str(self.inventory[item])}')
                # print("\n" + str(item) + " : " + str(self.inventory[item]))

class Pet():
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.maxHP = 2
        self.hp = 2
        self.attack = 1
        self.defence = 1
        self.maxEnergy = 5
        self.energy = 5
        self.exponent = 1.5
        self.baseXP = 1000
        self.xpIncrease = 1000

    def levelUpXP(self):
        return math.floor(self.baseXP * (float(self.level) ** self.exponent))

    def levelUp(self):
        self.level += 1
        # add leveling up more stats here
        self.energy = self.maxEnergy
        self.hp = self.maxHP
        print(f"CONGRADULATIONS! {self.name} has reached level {str(self.level)}!\n")

    def attk(self, enemy):
        hitChance = random.randint(0,10) - enemy.defence
        if hitChance > 3:
            enemy.hp -= self.attack
            if enemy.hp < self.attack:
                print(f"\n{self.name} killed the {enemy.type}. {self.name} has gained {str(self.xpIncrease)} XP!")
                self.xp += self.xpIncrease
            else:
                print(f"\n{self.name} hit the {enemy.type} for {str(self.attack)} damage!")
                enemy.attk(self)
        else:
            print(f"\n{self.name} missed!")
            enemy.attk(self)
        # Attempt to attack enemy
        # Uses energy

    def flee(self, enemy):
        # random chance to escape a battle
        if self.energy > 1:
            fleeChance = random.randint(0, 100)
            if fleeChance >= 50:
                print("\nYou successfully flee the battle!!")
                self.energy -= 1
                return "Success"
            else:
                # Enemy Attack
                print("\nYou are unsuccessfull..")
                self.energy -= 1
                enemy.attk(self)
        else:
            print("\nEnergy too low to flee!")

    def explore(self, playr):
        def battle():
            type = random.choice(["Snake","Rat","Badger"])
            enemy = Enemy(type)
            print(f"\nA wild {enemy.type} appeared!")
            while enemy.hp > 0 and self.hp > 0:
                print(f"\n{self.name}......................{enemy.type}")
                print(f"HP: {str(self.hp)}/{str(self.maxHP)}......................HP: {str(enemy.hp)}/{str(enemy.maxHP)}")
                print(f"Attack: {str(self.attack)}......................Attack: {str(enemy.attack)}")
                print(f"Defence: {str(self.defence)}......................Defence: {str(enemy.defence)}")
                print(f"Energy: {str(self.energy)}\n")

                battleChoice = input("What would you like to do? \n1. Attack \n2. Flee \n3. Use Item \n\n")

                if battleChoice == "1":
                    self.attk(enemy)
                elif battleChoice == "2":
                    if self.flee(enemy) == "Success":
                        break
                elif battleChoice == "3":
                    playr.useItem()
                else:
                    print("Please choose a number between 1 and 2")

        # Random chance to find enemy
        # Random chance to find candy
        # Decreases energy by 1
        if self.energy <= 0:
            print("\n" + self.name + " is too tired to explore right now!")
        else:
            chance = random.randint(0, 100)
            if chance > 80:
                print("\nYou found a candy!")
                return "CANDY"
            elif chance < 40:
                battle()
            else:
                print("\nYou wander around and find nothing special.")
            self.energy -= 1

    def rest(self):
        # Cannot rest if energy is full
        # Increases energy by 1
        if self.energy == self.maxEnergy:
            print("\n" + self.name + " is fully rested!")
        else:
            print("\n" + self.name + " takes a nap and feels refreshed..")
            healChance = random.randint(0,3)
            if healChance == 3 and self.hp < self.maxHP:
                self.hp += 1
            self.energy += 1


class Enemy():
    def __init__(self, type):
        self.type = type
        self.maxHP = 2
        self.hp = 2
        self.attack = 1
        self.defence = 1
        
    def attk(self, pet):
        hitChance = random.randint(0,10) - pet.defence
        if hitChance > 3:
            pet.hp -= self.attack
            print("\nThe " + self.type + " attacked " + pet.name + " for " + str(self.attack) + " damage!")
        else:
            print("\nThe " + self.type + " tried to attack " + pet.name + " but missed!")

class Game():

    def loop():
        def stats():
            print("\n" + yourPet.name)
            print("Level: " + str(yourPet.level))
            print("HP: " + str(yourPet.hp) + "/" + str(yourPet.maxHP))
            print("Energy: " + str(yourPet.energy) + "/" + str(yourPet.maxEnergy))
            print("Attack: " + str(yourPet.attack))
            print("Defence: " + str(yourPet.defence) + "\n")
        
        print("\nYou find a wild animal!")

        name = input("What is it's name? ")
        player = Player()
        yourPet = Pet(name)

        while yourPet.hp > 0:

            if yourPet.xp >= yourPet.levelUpXP():
                yourPet.levelUp()

            stats()

            choice = input("What would you like to do? \n1. Explore  \n2. Use an item \n3. Rest \n \n")

            if choice == "1":
                if yourPet.explore(player) == "CANDY":
                    # player.inventory.update({'candy': +1})
                        if "candy" not in player.inventory:
                            player.inventory['candy'] = 1
                        else:
                            player.inventory['candy'] += 1
            elif choice == "2":
                player.useItem()
            elif choice == "3":
                yourPet.rest()
            else:
                print("\nPlease enter a number between 1 and 3")
        
        stats()

        print(yourPet.name + " has died!")
        print("GAME OVER\n")

    loop()

if __name__ == "__main__":
    Game()