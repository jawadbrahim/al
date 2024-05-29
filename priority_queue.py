import heapq

class SorgicalRoom:
    def __init__(self):
        self.patients = []

    def add_patient(self, name, priority):
        heapq.heappush(self.patients, (priority, name))

    def next_patient(self):
        if self.patients:
            priority, name = heapq.heappop(self.patients)
            print("patient:", name)
    def is_empty(self):
        return not self.patients
    
sorgical_room =SorgicalRoom()
sorgical_room.add_patient("Jawad", 3)
sorgical_room.add_patient("Ali", 1)
sorgical_room.add_patient("Brahim",2)
while not sorgical_room.is_empty():
    sorgical_room.next_patient()
