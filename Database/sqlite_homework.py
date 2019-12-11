import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pprint import pprint

engine = create_engine('sqlite:////web/Sqlite-Data/example.db')
Session = sessionmaker(bind=engine)
session = Session()

# this loads the sqlalchemy base class
Base = declarative_base()

#Creating Customer class
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    address = Column(String(200), nullable=False)
    town = Column(String(50), nullable=False)

c1 = Customer(first_name = 'Toby',
              last_name = 'Miller',
              username = 'tmiller',
              email = 'tmiller@example.com',
              address = '1662 Kinney Street',
              town = 'Wolfden'
              )

c2 = Customer(first_name = 'Scott',
              last_name = 'Harvey',
              username = 'scottharvey',
              email = 'scottharvey@example.com',
              address = '424 Patterson Street',
              town = 'Beckinsdale'
              )
c1, c2

print(c1)
print(c2)
print(f'Firstname: {c1.first_name}, Lastname: {c1.last_name}')
print(f'Firstname: {c2.first_name}, Lastname: {c2.last_name}')


session.add(c1)
session.add(c2)
print(f'{c1.id}, {c2.id}')

