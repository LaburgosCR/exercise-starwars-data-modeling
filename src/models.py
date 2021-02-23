import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    Usuario_id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Genero = Column(String(250))
    Email = Column(String)
    Password = Column(String)
class personajes(Base):
    __tablename__ = 'personajes'
    personajes_id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Genero = Column(String(250))
    Masa = Column(Integer)
    color_cabello = Column(String)
    

class planetas(Base):
    __tablename__ = 'planetas'
    planetas_id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Diametro = Column(Integer)
    Clima = Column(String)
    Gravedad = Column(String)

class favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    Usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')