from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('mysql+pymysql://root:example@localhost:3306/cinema')
Session = sessionmaker(bind=engine)
session = Session()

#Entidades

class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme [(titulo={self.titulo}, ano={self.ano})]"

#SQL

#Insert
# data_insert = Filmes(titulo="Dracula", genero="Drama", ano=1996)
# session.add(data_insert)

#Delete
# session.query(Filmes).filter(Filmes.titulo=="Batman").delete()

#Update
session.query(Filmes).filter(Filmes.genero=="Drama").update({"ano": 2000})

#Finalizando
session.commit()

#Select
data = session.query(Filmes).all()
print(data)
print(data[0].titulo)

session.close()