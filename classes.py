class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    
    def seat_availability(self):
        return self.capacity - len(self.passengers)

    def addpassenger(self, name):
        self.passengers.append(name)
        if seat_availability == 0:
            return False
