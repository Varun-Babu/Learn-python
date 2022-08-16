#Exceptions

from tkinter import E


class CircuitBreaker:

    def __init__(self, max_amps):
        self.capacity = max_amps    #Max capacity in amps
        self.load = 0               #Present load in amps

    def connect(self,amps):
        if self.load + amps > self.capacity:
            raise Exception("Exceeds the capacity")
        elif self.load + amps < 0:
            raise Exception("Belo")     
        else:
            self.load += amps


cb = CircuitBreaker(20) #object1 with a max_amps of 20
cb.connect(10)
cb.connect(-15)