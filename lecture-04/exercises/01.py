#
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        validation_result = self.validate_contact(contact)
        if validation_result != "Відповідає":
            print(f"Контакт не відповідає: {validation_result}")
            return
        self.contacts.append(contact)
        print("Контакт додано успішно.")

    def clear_contacts(self):
        self.contacts = []

    def validate_contact(self, contact):
        required_fields = ["full_name", "phone_number"]
        for field in required_fields:
            if field not in contact or not contact[field]:
                return f"Поле '{field}' обовязково для запвнення."
        if not self.is_valid_phone_number(contact["phone_number"]):
            return "Номер телефона повинен бути числом длиной 12 символів."
        if self.is_duplicate_phone_number(contact["phone_number"]):
            return "Номер телефона є в списку."
        if self.is_duplicate_full_name(contact["full_name"]):
            return "Імя є в списку."
        return "Відповідає"

    def is_valid_phone_number(self, phone_number):
        if not phone_number.isdigit() or len(phone_number) != 12:
            return False
        return True

    def is_duplicate_phone_number(self, phone_number):
        for contact in self.contacts:
            if contact["phone_number"] == phone_number:
                return True
        return False

    def is_duplicate_full_name(self, full_name):
        for contact in self.contacts:
            if contact["full_name"] == full_name:
                return True
        return False

def add_contact_manually(manager):
    full_name = input("Введіть повне імя: ")
    phone_number = input("Введіть номер телефону: ")
    contact = {"full_name": full_name, "phone_number": phone_number}
    manager.add_contact(contact)

manager = ContactManager()
add_contact_manually(manager)
print(manager.contacts)
