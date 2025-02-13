class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def addpassenger(self, name):
        self.passengers.append(name)
        
    def seat_availability(self):
        return self.capacity - len(self.passengers)