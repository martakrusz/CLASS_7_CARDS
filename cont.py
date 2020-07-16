from faker import Faker

# My class
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
        return f"{self.__class__.__name__}(first_name={self.first_name} last_name={self.last_name}, email={self.email}, position={self.position})"    

fake = Faker()

person = Contact(first_name = fake.first_name(), 
                last_name = fake.last_name(),
                age = fake.random_int(min=40, max=99), 
                company = fake.company(), 
                position = fake.job(), 
                email = fake.email())

print(person)
person

#print(dir(Contact))

