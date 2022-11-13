from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.sql.sqltypes import DateTime
from flask_login import UserMixin


Base = declarative_base()

class Category(Base):
	__tablename__ = 'Category'
	ID = Column(Integer, nullable=False, primary_key=True)
	Type = Column(String(100), nullable=False)

	def __str__(self):
		return self.Type

class Products(Base):
	__tablename__ = 'Products'
	Game_ID = Column(Integer, nullable=False, primary_key=True)
	Name = Column(String(200), nullable=False)
	Price = Column(Float, nullable=False)
	Description = Column(String(200), nullable=True)
	Images = Column(String(100), default="no_image.png")
	Type_ID = Column(Integer, ForeignKey('Category.ID'), nullable=False)
	category = relationship(Category, backref='products')

	def __str__(self):
		return self.Name 

class Customer(Base):
    __tablename__ = 'Customer'
    Customer_ID = Column(Integer, primary_key=True)
    Fullname = Column(String(300), nullable=False)
    Username = Column(String(300), nullable=False)
    Password = Column(String(300), nullable=False)
    Email = Column(String(200))


class Order(Base):
    __tablename__ = 'Order'
    Order_ID = Column(Integer, primary_key=True)
    CustomerID = Column(Integer, ForeignKey('Customer.Customer_ID'))
    Order_date = Column(DateTime)
    Total = Column(Integer, nullable=False)
    customer = relationship(Customer, backref='order')


class Order_detail(Base):
    __tablename__ = 'Order_detail'
    Detail_ID = Column(Integer, primary_key=True)
    OrderID = Column(Integer, ForeignKey('Order.Order_ID'))
    GameID = Column(Integer, ForeignKey('Products.Game_ID'))
    Quantity = Column(Integer, nullable=False)
    Game_price = Column(Integer, nullable=False)
    Order_total = Column(Integer, nullable=False)
    product = relationship(Products, backref='order_detail')
    order = relationship(Order, backref='order_detail')

class ShopAdmin(Base, UserMixin):
    __tablename__ = 'ShopAdmin'
    id = Column(Integer, primary_key= True) 
    Fullname_Ad = Column(String(200), nullable=False)
    Username_Ad = Column(String(50), nullable=False) 
    Password_Ad = Column(String(50), nullable=False)


connect_var = 'mysql+pymysql://root:root@localhost:3306/gameshop'
engine = create_engine(connect_var)
Base.metadata.create_all(engine)