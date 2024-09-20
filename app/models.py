from sqlalchemy import Column, Integer, String, ForeignKey # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from .database import Base, SessionLocal

#Restaurant model
class Restaurant(Base):
    __tablename__ = "restaurants"

    #Primary key
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    menu = relationship("MenuItem", back_populates="restaurant")
    reservations = relationship("Reservation", back_populates="restaurant")

    #Name of the Restaurant
    def __repr__(self):
        return f"<Restaurant(id={self.id}, name='{self.name}')>"

    #Menu Items
    def add_menu_item(self, name, price):
        return MenuItem.create(name=name, price=price, restaurant_id=self.id)

    #Creating Reservation
    def create_reservation(self, customer_name, date_time):
        return Reservation.create(customer_name=customer_name, date_time=date_time, restaurant_id=self.id)


#MenuItem model
class MenuItem(Base):
    __tablename__ = "menu_items"

    #Primary Key
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    restaurant = relationship("Restaurant", back_populates="menu")


    def __repr__(self):
        return f"<MenuItem(id={self.id}, name='{self.name}', price={self.price})>"

    @classmethod
    def create(cls, name, price, restaurant_id):
        db = SessionLocal()
        item = cls(name=name, price=price, restaurant_id=restaurant_id)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

#Reservation model
class Reservation(Base):
    __tablename__ = "reservations"

    #Primary Key
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    date_time = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    restaurant = relationship("Restaurant", back_populates="reservations")

    def __repr__(self):
        return f"<Reservation(id={self.id}, customer_name='{self.customer_name}', date_time='{self.date_time}')>"

    @classmethod
    def create(cls, customer_name, date_time, restaurant_id):
        db = SessionLocal()
        reservation = cls(customer_name=customer_name, date_time=date_time, restaurant_id=restaurant_id)
        db.add(reservation)
        db.commit()
        db.refresh(reservation)
        return reservation
