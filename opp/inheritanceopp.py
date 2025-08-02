class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Breathing...")

class Fish(Animal):

    def __init__(self):
        super().__init__()  # Call the constructor of the parent class

    def swim(self):
        print("moving in water")

    def breath(self):   #this method overrides the parent class method
        super().breath()
        print("Breathing under water")


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)