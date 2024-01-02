class Animal:
    def feed(self):
        pass

class Cat(Animal):
    def feed(self):
        print("Abhishek is feeding Food to Cat")

class Dog(Animal):
    def feed(self):
        print("Abhishek is feeding Food to Dog")


def performaction(animal):
    animal.feed()

cat=Cat()
dog=Dog()

performaction(cat)
performaction(dog)
