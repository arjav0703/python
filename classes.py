class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    
    def seat_availability(self):
        return self.capacity - len(self.passengers)

    def addpassenger(self, name):
        if seat_availability() == 0:
            return False
        self.passengers.append(name)
        return True

pirate_air = Flight(40)

ppl = ['Arjav', 'Anay', 'Satat', 'Daksh', 'Vaibhav', 'Apoorv']