import random
class fakeGyro:
    def getValue(self):
        return [random.randint(1,100), random.randint(1,100), random.randint(1,100)]