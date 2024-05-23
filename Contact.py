class Contact():
    def __init__(self, first_name, last_name, phone=None, email=None, display_mode="mask"):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.display_mode = display_mode

    def __repr__(self):
        return f"Contact(first_name={self.first_name}, last_name={self.last_name})"

    def __str__(self):
        return f"{self.last_name[0]}{self.first_name[0]}"

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        elif (self.email and other.email and self.email == other.email) or (self.phone and other.phone and self.phone == other.phone):
            return True
        elif self.first_name == other.first_name and self.last_name == other.last_name:
            return True
        else:
            return False

    def __format__(self, format_spec):
        if format_spec == "unmasked":
            return f"Contact(first_name={self.first_name}, last_name={self.last_name}, phone={self.phone}, email={self.email})"
        else:
            return self.__repr()
