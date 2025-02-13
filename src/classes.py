class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    
    def addpassenger(self, name):
        if not self.seat_availability():
            return False
        self.passengers.append(name)
        return True
    def seat_availability(self):
        return self.capacity - len(self.passengers)

pirate_air = Flight(40)

ppl = ['Arjav', 'Anay', 'Satat', 'Daksh', 'Vaibhav', 'Apoorv']

for callsign in ppl:
    if pirate_air.addpassenger(callsign):
        print(f"Added {callsign} to the flight")
    else:
        print(f"No available seats for {callsign}")