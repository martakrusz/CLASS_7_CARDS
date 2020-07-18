from faker import Faker

class Contact:
    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.position}'    

class BaseContact(Contact):
    def __init__(self,phone,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.phone = phone
    
    @property
    def name_len(self):
        return sum([len(self.first_name), len(self.last_name)],1)

    def contact(self):
        return f'Wybieram numer +48 {self.phone} i dzwonię do {self.first_name} {self.last_name}'

class BusinessContact(Contact):
    def __init__(self,busines_phone,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.busines_phone = busines_phone
    
    @property
    def name_len(self):
        return sum([len(self.first_name), len(self.last_name)],1)

    def contact(self):
        return f'Wybieram numer +48 {self.busines_phone} i dzwonię do {self.first_name} {self.last_name}'



fake = Faker()
number = int(input("Input number of cards: "))
for _ in range(number):
    person = Contact(first_name = fake.first_name(), 
                    last_name = fake.last_name(), 
                    company = fake.company(), 
                    position = fake.job(), 
                    email = fake.email()
                    )
    print(f'{person.first_name}, {person.last_name}, {person.email}, {person.position},\n')            



wizit1 = BaseContact(first_name = fake.first_name(), 
                    last_name = fake.last_name(),
                    company = fake.company(),
                    position = fake.job(), 
                    email = fake.email(),
                    phone = fake.random_int(min=100000000, max=999999999)
                    )

wizit2 = BusinessContact(first_name = fake.first_name(), 
                    last_name = fake.last_name(), 
                    company = fake.company(),
                    position = fake.job(), 
                    email = fake.email(),
                    busines_phone = fake.random_int(min=100000000, max=999999999)
                    )
#print(wizit1.first_name, wizit1.last_name, wizit1.email, wizit1.name_len, wizit1.phone)
#print(wizit2.first_name, wizit2.last_name, wizit2.email, wizit2.name_len, wizit2.busines_phone)
#print(BaseContact.contact(wizit1))
#print(BusinessContact.contact(wizit2))