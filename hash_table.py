class HashTable:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number

    def search_by_name(self, name):
        return self.contacts.get(name, "Contact not found")

    def search_by_number(self, phone_number):
        for name, number in self.contacts.items():
            if number == phone_number:
                return name
        return "Contact not found"

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact", name, "removed successfully")
        else:
            print("Contact", name, "not found")
hashtable = HashTable()
hashtable.add_contact("ali", "70123456")
hashtable.add_contact("brahim", "71189102")
hashtable.add_contact("jawad", "81201843")
print("Search for ali:", hashtable.search_by_name("ali"))
print("Search for brahim:", hashtable.search_by_name("brahim"))
print("Search for jawad:", hashtable.search_by_name("jawad"))
print("Search by phone number '70123456':", hashtable.search_by_number("70123456"))
hashtable.remove_contact("jawad")
