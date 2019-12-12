from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. Created engine for sqlite
engine = create_engine('sqlite:////web/Sqlite-Data/example.db')
Session = sessionmaker(bind=engine)
session = Session()

# this loads the sqlalchemy base class
Base = declarative_base()

# 2. Inserting Data into customer
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


Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

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

# 3. Adding objects into session
session.add(c1)
session.add(c2)
print(f'{c1.id}, {c2.id}')

#4 creating new session and commiting it
session.add_all([c1, c2])
session.new
session.commit()

c3 = Customer(
    first_name = "John",
    last_name = "Lara",
    username = "johnlara",
    email = "johnlara@mail.com",
    address = "3073 Derek Drive",
    town = "Norfolk"
)

c4 = Customer(
    first_name = "Sarah",
    last_name = "Tomlin",
    username = "sarahtomlin",
    email = "sarahtomlin@mail.com",
    address = "3572 Poplar Avenue",
    town = "Norfolk"
)

c5 = Customer(first_name = 'Toby',
              last_name = 'Miller',
              username = 'tmiller',
              email = 'tmiller@example.com',
              address = '1662 Kinney Street',
              town = 'Wolfden'
              )

c6 = Customer(first_name = 'Scott',
              last_name = 'Harvey',
              username = 'scottharvey',
              email = 'scottharvey@example.com',
              address = '424 Patterson Street',
              town = 'Beckinsdale'
              )

session.add_all([c3, c4, c5, c6])
session.commit()