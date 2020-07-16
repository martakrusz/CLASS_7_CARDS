from faker import Faker

class Contact:
    def __init__(self, first_name, last_name, age, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.company = company
        self.position = position
        self.email = email

    def __str__(self):
        return f'{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.position}\n{self.company}'

    def __repr__(self):
        return f"{self.__class__.__name__}(first_name={self.first_name} last_name={self.last_name}, age={self.age}, company={self.company} email={self.email}, position={self.position})"    

    def __eq__(self,other):
        return(
            self.first_name == other.first_name and
            self.last_name == other.last_name and
            self.age == other.age and
            self.company == other.company and
            self.position == other.position and
            self.email == other.email
        )

    def __gt__(self, other):
        return self.age > other.age

fake = Faker()

person1 = Contact(first_name = "Marta", 
                last_name = "Krusz",
                age = 35, 
                company = "Merk", 
                position = "Specjal", 
                email = "mart@mart")

person2 = Contact(first_name = "Ania", 
                last_name = "Frusz",
                age = 38, 
                company = "Merk", 
                position = "Specjal", 
                email = "mart@mart")

persons = [person1, person2]
print(person1)

print(person1 == person2)

print(person1 > person2)

by_age = sorted(persons,key=lambda Contact: Contact.age)
by_first_name = sorted(persons,key=lambda Contact: Contact.first_name)
by_last_name = sorted(persons,key=lambda Contact: Contact.last_name)

print(by_age)
print(by_first_name)
print(by_last_name)