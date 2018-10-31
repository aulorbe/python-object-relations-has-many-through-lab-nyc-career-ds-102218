# import Trip class here
from trip import Trip

class Passenger:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def trips(self): #returns a list of trip objects for input passenger
        return [trip for trip in Trip._all if trip.passenger == self]

    def drivers(self):
        return [trip.driver for trip in Trip._all if trip.passenger == self]

    def trip_count(self):
        return len(self.trips())

        
#SETTERS
    @property
    def name (self):
        return self._name

    @property
    def age(self):
        return self._age


# GETTERS
    @name.setter
    def name(self, name):
        self._name = _name

    @age.setter
    def age(self,age):
        self._age = age
