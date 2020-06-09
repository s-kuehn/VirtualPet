import random

class Player():
    def __init__(self):
        self.inventory = {}

    def useItem(self):
        # Print player inventory and use items
        if self.inventory == {}:
            print("\nInventory is empty..")
        else:
            print("\nCurrent Items:")
            for item in self.inventory:
                print("\n" + str(item) + " : " + str(self.inventory[item]))

class Pet():
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.maxHP = 2
        self.hp = 2
        self.attack = 1
        self.defence = 1
        self.maxEnergy = 5
        self.energy = 5

    def attk(self, enemy):
        hitChance = random.randint(0,10) - enemy.defence
        if hitChance > 4:
            enemy.hp -= self.attack
            if enemy.hp <= self.attack:
                print("\n" + self.name + " killed the " + enemy.type)
            else:
                print("\n" + "Hit " + enemy.type + "!")
        else:
            print("\n" + self.name + " missed!")
        # Attempt to attack enemy
        # Uses energy

    def flee(self):
        # random chance to escape a battle
        if self.energy > 1:
            fleeChance = random.randint(0, 100)
            if fleeChance >= 75:
                print("\nYou successfully flee the battle!!")
                self.energy -= 1
                return "Success"
            else:
                # Enemy Attack

                print("\nYou are unsuccessfull..")
                self.energy -= 1
        else:
            print("\nEnergy too low to flee!")

    def explore(self):
        def battle():
            type = random.choice(["Snake","Rat","Badger"])
            enemy = Enemy(type)
            print("\nA wild " + enemy.type + " appeared!")
            while enemy.hp > 0:
                print("\n" + self.name + "......................" + enemy.type)
                print("HP: " + str(self.hp) + "/" + str(self.maxHP) + "......................" + "HP: " + str(enemy.hp) + "/" + str(enemy.maxHP))
                print("Attack: " + str(self.attack) + "......................" + "Attack: " + str(enemy.attack))
                print("Defence: " + str(self.defence) + "......................" + "Defence: " + str(enemy.defence))
                print("Energy: " + str(self.energy) + "\n")

                battleChoice = raw_input("What would you like to do? \n1. Attack \n2. Flee\n\n")

                if battleChoice == "1":
                    self.attk(enemy)
                elif battleChoice == "2":
                    if self.flee() == "Success":
                        break
                    # if self.flee() == "Success":
                    #     print("\nYou successfully flee the battle!!")
                    #     self.energy -= 1
                    #     break
                    # else:
                    #     self.energy -= 1
                    #     print("\nYou are unsuccessfull..")
                    # elif self.flee() == "LowEnergy":
                    #     print("\nEnergy too low to flee!")

                        
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
        # Increases energy by 1
        if self.energy == self.maxEnergy:
            print("\n" + self.name + " is fully rested!")
        else:
            print("\n" + self.name + " takes a nap and feels refreshed..")
            self.energy += 1
        # Cannot rest if energy is full


class Enemy():
    def __init__(self, type):
        self.type = type
        self.maxHP = 2
        self.hp = 1
        self.attack = 1
        self.defence = 1
        
    def attack():
        pass

class Game():

    def loop():
        def stats():
            print("\n" + yourPet.name)
            print("HP: " + str(yourPet.hp) + "/" + str(yourPet.maxHP))
            print("Energy: " + str(yourPet.energy) + "/" + str(yourPet.maxEnergy))
            print("Attack: " + str(yourPet.attack))
            print("Defence: " + str(yourPet.defence) + "\n")
        
        print("\nYou find a wild animal!")

        name = raw_input("What is it's name? ")
        player = Player()
        yourPet = Pet(name)

        while yourPet.hp > 0:
            stats()

            choice = raw_input("What would you like to do? \n1. Explore  \n2. Use an item \n3. Rest \n \n")

            if choice == "1":
                if yourPet.explore() == "CANDY":
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