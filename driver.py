# remeber to import the Trip class here
from trip import Trip

class Driver:

    def __init__(self, name, driving_style):
        self._name = name
        self._driving_style = driving_style

# INSTANCE METHODS
    def trips(self): #returns all of driver's trips
        return [trip for trip in Trip._all if trip.driver == self]



    def passengers(self): #list of passengers who rode with input
        return [trip.passenger for trip in Trip._all if trip.driver == self]

    def trip_count(self):
        return len(self.trips())

#SETTERS
    @property
    def name (self):
        return self._name

    @property
    def driving_style (self):
        return self._driving_style



#GETTERS
    @name.setter
    def name(self,name):
        self._name = name

    @driving_style.setter
    def name(self,driving_style):
        self._driving_style = driving_style
