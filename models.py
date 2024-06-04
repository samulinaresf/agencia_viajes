from numbers import Real
from sqlalchemy import Column, Integer, String, ForeignKey
import db

#Creating the table Countries
class Countries(db.Base):
    __tablename__ = "Countries"
    __table_args__ = {'sqlite_autoincrement':True}
    country_id = Column(Integer,primary_key=True,autoincrement=True)
    country_name = Column(String,nullable=False)
    country_code = Column(String,nullable=False)

    def __int__(self,country_id,country_name,country_code):
        self.country_id = country_id
        self.country_name = country_name
        self.country_code = country_code
    def __str__(self):
        return f"¡Country created!\nID: {self.country_id}\nName: {self.country_name}\nCode: {self.country_code}"

#Creating the table Employees
class Employees(db.Base):
    __tablename__ = "Employees"
    __table_args__ = {'sqlite_autoincrement':True}
    employee_id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    surname = Column(String,nullable=False)
    passport_number = Column(String,nullable=False)
    email = Column(String,nullable=True)
    phone_number = Column(String,nullable=True)
    birth_date = Column(Integer)
    occupation = Column(String,nullable=False)
    hiring_date = Column(Integer)
    studies = Column(String,nullable=True)
    notes = Column(String,nullable=True)

#Creating the table Customers
class Customers(db.Base):
    __tablename__ = "Customers"
    __table_args__ = {'sqlite_autoincrement':True}
    customer_id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    surname = Column(String,nullable=False)
    birth_date = Column(Integer)
    passport_number = Column(String,nullable=False)
    email = Column(String,nullable=True)
    phone_number = Column(String,nullable=True)
    country_id = Column(Integer,ForeignKey(Countries.country_id))
    notes = Column(String,nullable=True)


#Creating the table Orders
class Orders(db.Base):
    __tablename__ = "Orders"
    __table_args__ = {'sqlite_autoincrement':True}
    order_id = Column(Integer,primary_key=True,autoincrement=True)
    order_details = Column(String,nullable=False)
    employee_id = Column(Integer, ForeignKey(Employees.employee_id))
    customer_id = Column(Integer, ForeignKey(Customers.customer_id))
    country_id = Column(Integer, ForeignKey(Countries.country_id))
    order_date = Column(Integer)
    notes = Column(String,nullable=True)

#Creating the table Airlines
class Airlines(db.Base):
    __tablename__ = "Airlines"
    __table_args__ = {'sqlite_autoincrement':True}
    airline_id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    phone_number = Column(String, nullable=True)
    email = Column(String, nullable=True)
    notes = Column(String, nullable=True)

#Creating the table Flights
class Flights(db.Base):
    __tablename__ = "Flights"
    __table_args__ = {'sqlite_autoincrement':True}
    flight_id = Column(Integer,primary_key=True,autoincrement=True)
    flight_type = Column(String,nullable=False)
    price = Column(Real)
    date = Column(Integer)
    airport = Column(String,nullable=False)
    airline_id = Column(Integer, ForeignKey(Airlines.airline_id))
    order_id = Column(Integer,ForeignKey(Orders.order_id))

#Creating the table Accommodation_companies
class Accommodation_companies(db.Base):
    __tablename__ = "Accommodation_companies"
    __table_args__ = {'sqlite_autoincrement':True}
    company_id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    type = Column(String,nullable=False)
    category = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey(Countries.country_id))
    location = Column(String,nullable=False)
    description = Column(String,nullable=False)
    phone_number = Column(String,nullable=True)
    email = Column(String,nullable=True)

#Creating the table Accommodation_bookings
class Accommodation_bookings(db.Base):
    __tablename__ = "Accommodation_bookings"
    __table_args__ = {'sqlite_autoincrement':True}
    booking_id = Column(Integer,primary_key=True,autoincrement=True)
    company_id = Column(Integer, ForeignKey(Accommodation_companies.company_id))
    number_nights = Column(Integer)
    type_room = Column(String,nullable=False)
    number_guests = Column(Integer)
    boarding_base = Column(String,nullable=False)
    price = Column(Real)
    checkin_date = Column(Integer)
    checkout_date = Column(Integer)
    order_id = Column(Integer,ForeignKey(Orders.order_id))
    notes = Column(String,nullable=True)

#Creating the table Activities_companies
class Activities_companies(db.Base):
    __tablename__ = "Activities_companies"
    __table_args__ = {'sqlite_autoincrement':True}
    company_id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    type = Column(String,nullable=False)
    country_id = Column(Integer, ForeignKey(Countries.country_id))
    phone_number = Column(String,nullable=True)
    email = Column(String,nullable=True)
    notes = Column(String,nullable=True)

#Creating the table Activities
class Activities(db.Base):
    __tablename__ = "Activities"
    __table_args__ = {'sqlite_autoincrement':True}
    activity_id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    price = Column(Real)
    date = Column(Integer)
    category = Column(String,nullable=False)
    location = Column(String,nullable=False)
    company_id = Column(Integer, ForeignKey(Activities_companies.company_id))
    order_id = Column(Integer, ForeignKey(Orders.order_id))
    notes = Column(String,nullable=True)



