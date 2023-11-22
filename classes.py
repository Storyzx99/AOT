#AOT Project
class Titan:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def take_damage(self, damage):
            self.health = self.health - damage
    

#testing objects
titan = Titan("Eren", 100, 50)
print(titan.name)

print("Orignal Health",titan.health)
titan.take_damage(10)
print(f'new health: {titan.health}')
print(titan.power)