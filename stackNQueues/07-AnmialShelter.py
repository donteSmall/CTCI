import unittest

class AnimalShelter():
    def __init__(self):
        self.cats =[]
        self.dogs =[]

    def enqueue(self,animal):
        if animal.__class__ == Cat:
            self.cats.append(animal)
        else:
            self.dogs.append(animal)


    def dequeueAny(self):
        if len(self.cats):
            return self.dequeueCats()
        else:
            return self.dequeueDog()


    def dequeueCats(self):
        if len(self.cats) == 0:
            return None

        first_Cat_In_Quene = self.cats[0]
        #moves cat pointer to the second indx and iterates entire list
        self.cats = self.cats[1:]
        return first_Cat_In_Quene

    def dequeueDog(self):
            if len(self.dogs) == 0:
                return None
            first_Dog_In_Quene = self.dogs[0]

            #moves dogs pointer to the second indx and iterates entire list
            self.dogs = self.dogs[1:]
            return first_Dog_In_Quene


class Animal():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Cat(Animal):pass
class Dog(Animal):pass

class Test(unittest.TestCase):
     def setUp(self):
        self.shelter = AnimalShelter()

     def test_DequeueAny(self):
        self.shelter.enqueue(Cat("Blue"))
        self.shelter.enqueue(Dog("Fish"))
        self.shelter.enqueue(Dog("Red"))
        self.shelter.enqueue(Cat("Dish"))
        self.assertEqual(str(self.shelter.dequeueAny()),"Blue")
        self.assertEqual(str(self.shelter.dequeueAny()),"Dish")

     def test_enqueueCat(self):
        self.shelter.enqueue(Dog("Blue"))
        self.shelter.enqueue(Dog("Fish"))
        self.shelter.enqueue(Dog("Red"))
        self.shelter.enqueue(Cat("Dish"))
        self.assertEqual(str(self.shelter.dequeueCats()),"Dish")

     def test_DequeueCat(self):
       self.shelter.enqueue(Cat("Blue"))
       self.shelter.enqueue(Cat("Fish"))
       self.shelter.enqueue(Cat("Red"))
       self.shelter.enqueue(Cat("Dish"))
       self.assertEqual(str(self.shelter.dequeueDog()),'None')
       self.shelter.enqueue(Dog("Red"))
       self.assertEqual(str(self.shelter.dequeueDog()),'Red')


if __name__=="__main__":
    unittest.main()
