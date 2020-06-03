class VirtualPet():
    def __init__(self):
        self.hunger = 10
        self.thirst = 10
        self.boredom = 10

    def feed(self):
        self.thirst += 3
        self.boredom += 2
        if self.hunger > 0:
            self.hunger -= 5
            print(" ")
            print("Pixel eats some food..")
        else:
            print(" ")
            print("Pixel has ate enough!")

    def water(self):
        self.hunger += 3
        self.boredom += 2
        if self.thirst > 0:
            self.thirst -= 5
            print(" ")
            print("Pixel drinks the water..")
        else:
            print(" ")
            print("Pixel has drank enough!")

    def play(self):
        self.hunger += 3
        self.thirst += 2
        if self.boredom > 0:
            self.boredom -= 5
            print(" ")
            print("Pixel is thoroughly entertained..")
        else:
            print(" ")
            print("Pixel has played enough!")

    def tick(self, action):
        if action == '1':
            self.feed()
        if action == '2':
            self.water()
        if action == '3':
            self.play()

class VirtualPetApp():
    def main():
        pet = VirtualPet()
        while True:

            print(" ")

            print("Pixel The Cat")
            print("Hunger: " + str(pet.hunger))
            print("Thirst: " + str(pet.thirst))
            print("boredom: " + str(pet.boredom))

            print(" ")

            choice = raw_input("""What do you want to do?
    1. Feed pet
    2. Water pet
    3. Play with Pet

    """)
            pet.tick(choice)
    main()

VirtualPetApp()