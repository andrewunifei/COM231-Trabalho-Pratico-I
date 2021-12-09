from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from exibir import bootloader_exibir
from filtros import bootloader_filtros

def getSession(user, senha):
    dburi = "postgresql+psycopg2://{user}:{senha}@localhost:5432/yelp".format(user=user, senha=senha)
    engine = create_engine(dburi, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session, dburi

def insere(sessao, obj):
    sessao.add(obj)

def deleta(session, obj):
    session.delete(obj)

def main(user,  senha, nome_tabela, valores_exibir, valores_filtros, lista_atributos):
    session, dburi = getSession(user, senha) 

    info_exibir = bootloader_exibir(session, dburi, nome_tabela, valores_exibir)
    info_filtros = bootloader_filtros(session, nome_tabela, valores_filtros)

    return info_exibir, info_filtros