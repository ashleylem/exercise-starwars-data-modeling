import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey("favorites.user_id"), primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__="favorites"
    user_id = Column(Integer, primary_key=True)
    favorite_character= Column(String(250))
    favorite_planet= Column(String(250))
    favorite_vehicle= Column(String(250))


class Planets(Base):
    __tablename__="planets"
    date_added= Column(DateTime(False))
    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey("favorites.favorite_planet"), nullable=False)
    #nullable is for things that cannot be blank
    size= Column(Integer)
    population= Column(Integer)
    climate= Column(String(250))

class Vehicle(Base):
    __tablename__="vehicle"
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey("favorites.favorite_vehicle"), nullable=False)
    pilot= Column(String(250))
    vehicle_type= Column(String(250))

class Character(Base):
    __tablename__="character"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey("vehicle.pilot"),  ForeignKey("favorites.favorite_character"), nullable=False)
    #nullable is for things that cannot be blank
    planet_from= Column(String(250), ForeignKey("planet.name"))
    age= Column(Integer)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
