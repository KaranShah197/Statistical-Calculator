from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

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
    orders = relationship("Order", backref='customer')

# Item Table
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer(), nullable=False)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now, nullable=False)
    date_shipped = Column(DateTime())


class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(Integer())
    order = relationship("Order", backref='order_lines')
    item = relationship("Item")

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

i1 = Item(name = 'Chair', cost_price = 9.21, selling_price = 10.81, quantity = 5)
i2 = Item(name = 'Pen', cost_price = 3.45, selling_price = 4.51, quantity = 3)
i3 = Item(name = 'Headphone', cost_price = 15.52, selling_price = 16.81, quantity = 50)
i4 = Item(name = 'Travel Bag', cost_price = 20.1, selling_price = 24.21, quantity = 50)
i5 = Item(name = 'Keyboard', cost_price = 20.1, selling_price = 22.11, quantity = 50)
i6 = Item(name = 'Monitor', cost_price = 200.14, selling_price = 212.89, quantity = 50)
i7 = Item(name = 'Watch', cost_price = 100.58, selling_price = 104.41, quantity = 50)
i8 = Item(name = 'Water Bottle', cost_price = 20.89, selling_price = 25, quantity = 50)

session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
session.commit()

o1 = Order(customer = c1)
o2 = Order(customer = c1)

line_item1 = OrderLine(order = o1, item = i1, quantity =  3)
line_item2 = OrderLine(order = o1, item = i2, quantity =  2)
line_item3 = OrderLine(order = o2, item = i1, quantity =  1)
line_item3 = OrderLine(order = o2, item = i2, quantity =  4)

session.add_all([o1, o2])

session.new
session.commit()

o3 = Order(customer = c1)
orderline1 = OrderLine(item = i1, quantity = 5)
orderline2 = OrderLine(item = i2, quantity = 10)

o3.order_lines.append(orderline1)
o3.order_lines.append(orderline2)

session.add_all([o3])

session.commit()

print(f'{c1.orders}')
print(f'{o1.customer}')
print(f'{c1.orders[0].order_lines}, {c1.orders[1].order_lines}')

for ol in c1.orders[0].order_lines:
    print(f'{ol.id}, {ol.item}, {ol.quantity}')

print('-------')

for ol in c1.orders[1].order_lines:
    print(f'{ol.id}, {ol.item}, {ol.quantity}')

#Quering functions
session.query(Customer).all()
print(session.query(Customer))
q = session.query(Customer)

for c in q:
    print(c.id, c.first_name)

session.query(Customer.id, Customer.first_name).all()

session.query(Customer).count() # get the total number of records in the customers table
session.query(Item).count()  # get the total number of records in the items table
session.query(Order).count()  # get the total number of records in the orders table