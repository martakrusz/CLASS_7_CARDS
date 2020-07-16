from faker import Faker

class Contact:
    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'    

fake = Faker()

for _ in range(5):
    person = Contact(first_name = fake.first_name(), 
                    last_name = fake.last_name(), 
                    company = fake.company(), 
                    position = fake.job(), 
                    email = fake.email())
    print(person.first_name, person.last_name, person.email, person.position)

print(dir(Contact))



