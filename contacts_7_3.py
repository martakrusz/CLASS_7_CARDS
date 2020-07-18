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

for _ in range(5):
    person = Contact(first_name = fake.first_name(), 
                    last_name = fake.last_name(), 
                    company = fake.company(), 
                    position = fake.job(), 
                    email = fake.email()
                    )


def create_contacts():
    number = int(input("Input number of cards: "))
    card = int(input("Input kidn of card for Bisines input 1, for Private input 2: "))
    if card == 1:
        for _ in range(number):
            base = BaseContact(first_name = fake.first_name(), 
                    last_name = fake.last_name(),
                    company = fake.company(),
                    position = fake.job(), 
                    email = fake.email(),
                    phone = fake.random_int(min=100000000, max=999999999)
                    )
            print(base.first_name, base.last_name, base.email, base.name_len, base.phone)
    if card == 2:
        for _ in range(number):
            business = BusinessContact(first_name = fake.first_name(), 
                    last_name = fake.last_name(), 
                    company = fake.company(),
                    position = fake.job(), 
                    email = fake.email(),
                    busines_phone = fake.random_int(min=100000000, max=999999999)
                    )
            print(business.first_name, business.last_name, business.email, business.name_len, business.busines_phone)


create_contacts()
