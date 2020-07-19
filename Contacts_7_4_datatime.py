from faker import Faker
import datetime
import time

class Contact:
    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email 


fake = Faker()

start = datetime.datetime.now()
def card():
    for wizit_card in range(100):
        person = Contact(first_name = fake.first_name(), 
                        last_name = fake.last_name(), 
                        company = fake.company(), 
                        position = fake.job(), 
                        email = fake.email()
                        )
        print(f'{person.first_name}, {person.last_name}, {person.email}, {person.position}')


def time_machine(func):
    def wrapper():
        start_fun = time.time()
        func()
        print ("Funcjon took:", time.time() - start_fun, "seconds")
    return wrapper


@time_machine
def card():
    for wizit_card in range(100):
        person = Contact(first_name = fake.first_name(), 
                        last_name = fake.last_name(), 
                        company = fake.company(), 
                        position = fake.job(), 
                        email = fake.email()
                        )
        print(f'{person.first_name}, {person.last_name}, {person.email}, {person.position}')

card()    
