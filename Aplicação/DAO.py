from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

class DAOCrud():
    def getSession():
        engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/yelp", echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def insere(sessao, obj):
        sessao.add(obj)

    def deleta(session, obj):
        session.delete(obj)