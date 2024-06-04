# Importando los métodos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Creando el engine para conectarme a la base de datos
engine = create_engine("sqlite:///database/agencia_viajes.db")

# Creando la Session
Session = sessionmaker(bind=engine)

# Creando la Base
Base = declarative_base()