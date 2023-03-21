import random

class SpO2Randomizer:
    def __init__(self, startSpO2, minSpO2, maxSpO2, delta):
        self.SpO2 = startSpO2
        self.minSpO2 = minSpO2
        self.maxSpO2 = maxSpO2
        self.delta = delta

    def SpO2Generator(self):
        change = random.random()*2*self.delta-self.delta
        self.SpO2 = self.SpO2 + change
        if self.SpO2 < self.minSpO2:
            self.SpO2 = self.SpO2 + self.delta
        elif self.SpO2 > self.maxSpO2:
            self.SpO2 = self.SpO2 - self.delta
        return str(round(self.SpO2))

s = SpO2Randomizer(98, 95, 100, 1)

f = open("SpO2.txt","w")

for i in range(100):
    f.write(s.SpO2Generator()+"\n")

f.close()

