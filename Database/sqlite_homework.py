from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Numeric, or_, and_, not_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy import text
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

session.query(Customer).first()
session.query(Item).first()
session.query(Order).first()

session.query(Customer).get(1)
session.query(Item).get(1)
session.query(Order).get(100)

session.query(Customer).filter(Customer.first_name == 'John').all()
print(session.query(Customer).filter(Customer.first_name == 'John'))

session.query(Customer).filter(Customer.id <= 5, Customer.town == "Norfolk").all()
print(session.query(Customer).filter(Customer.id <= 5, Customer.town.like("Nor%")))

# find all customers who either live in Peterbrugh or Norfolk

session.query(Customer).filter(or_(
    Customer.town == 'Peterbrugh',
    Customer.town == 'Norfolk'
)).all()


# find all customers whose first name is John and live in Norfolk

session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    Customer.town == 'Norfolk'
)).all()


# find all johns who don't live in Peterbrugh

session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    not_(
        Customer.town == 'Peterbrugh',
        )
)).all()


session.query(Order).filter(Order.date_shipped == None).all()
session.query(Order).filter(Order.date_shipped != None).all()

session.query(Customer).filter(Customer.first_name.in_(['Toby', 'Sarah'])).all()
session.query(Customer).filter(Customer.first_name.notin_(['Toby', 'Sarah'])).all()

#Between
session.query(Item).filter(Item.cost_price.between(10, 50)).all()
session.query(Item).filter(Item.cost_price.between(10, 50)).all()

#Like
session.query(Item).filter(Item.name.like("%r")).all()
session.query(Item).filter(Item.name.ilike("w%")).all()
session.query(Item).filter(not_(Item.name.like("W%"))).all()

#LIMIT function
session.query(Customer).limit(2).all()
session.query(Customer).filter(Customer.address.ilike("%avenue")).limit(2).all()

#Offset
session.query(Customer).limit(2).offset(2).all()
print(session.query(Customer).limit(2).offset(2))

#orderby
session.query(Item).filter(Item.name.ilike("wa%")).all()
session.query(Item).filter(Item.name.ilike("wa%")).order_by(Item.cost_price).all()

from sqlalchemy import desc
session.query(Item).filter(Item.name.ilike("wa%")).order_by(desc(Item.cost_price)).all()

#Join
session.query(Customer).join(Order).all()
print(session.query(Customer).join(Order))
session.query(Customer.id, Customer.username, Order.id).join(Order).all()
session.query(
    Customer.first_name,
    Item.name,
    Item.selling_price,
    OrderLine.quantity
).join(Order).join(OrderLine).join(Item).filter(
    Customer.first_name == 'John',
    Customer.last_name == 'Green',
    Order.id == 1,
).all()

#Outer Join
session.query(
    Customer.first_name,
    Order.id,
).outerjoin(Order).all()

session.query(
    Customer.first_name,
    Order.id,
).outerjoin(Order, full=True).all()

#group by
from sqlalchemy import func

session.query(func.count(Customer.id)).join(Order).filter(
    Customer.first_name == 'John',
    Customer.last_name == 'Green',
).group_by(Customer.id).scalar()

# find the number of customers lives in each town

session.query(
    func.count("*").label('town_count'),
    Customer.town
).group_by(Customer.town).having(func.count("*") > 2).all()


#duplicate check
from sqlalchemy import distinct

session.query(Customer.town).filter(Customer.id  < 10).all()
session.query(Customer.town).filter(Customer.id  < 10).distinct().all()

session.query(
    func.count(distinct(Customer.town)),
    func.count(Customer.town)
).all()

#Casting
from sqlalchemy import cast, Date, distinct, union

session.query(
    cast(func.pi(), Integer),
    cast(func.pi(), Numeric(10,2)),
    cast("2010-12-01", DateTime),
    cast("2010-12-01", Date),
).all()

#Unions
s1 = session.query(Item.id, Item.name).filter(Item.name.like("Wa%"))
s2 = session.query(Item.id, Item.name).filter(Item.name.like("%e%"))
s1.union(s2).all()

#union all
s1.union_all(s2).all()

#updating the data
i = session.query(Item).get(8)
i.selling_price = 25.91
session.add(i)
session.commit()

# update quantity of all quantity of items to 60 whose name starts with 'W'

session.query(Item).filter(
    Item.name.ilike("W%")
).update({"quantity": 60}, synchronize_session='fetch')
session.commit()

#deleting the data
i = session.query(Item).filter(Item.name == 'Monitor').one()
i
session.delete(i)
session.commit()

session.query(Item).filter(
    Item.name.ilike("W%")
).delete(synchronize_session='fetch')
session.commit()

#Raw Queries
session.query(Customer).filter(text("first_name = 'John'")).all()
session.query(Customer).filter(text("town like 'Nor%'")).all()
session.query(Customer).filter(text("town like 'Nor%'")).order_by(text("first_name, id desc")).all()