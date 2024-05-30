class AddressBook:
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
address_book = AddressBook()
address_book.add_contact("ali", "70123456")
address_book.add_contact("brahim", "71189102")
address_book.add_contact("jawad", "81201843")
print("Search for ali:", address_book.search_by_name("ali"))
print("Search for brahim:", address_book.search_by_name("brahim"))
print("Search for jawad:", address_book.search_by_name("jawad"))
print("Search by phone number '70123456':", address_book.search_by_number("70123456"))
address_book.remove_contact("jawad")
