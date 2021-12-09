from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from exibir import bootloader_exibir
from filtros import bootloader_filtros

def getSession(password):
    dburi = "postgresql+psycopg2://postgres:{password}@localhost:5432/yelp".format(password=password)
    engine = create_engine(dburi, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session, dburi

def insere(sessao, obj):
    sessao.add(obj)

def deleta(session, obj):
    session.delete(obj)

def main(password, nome_tabela, valores_exibir, valores_filtros):
    session, dburi = getSession(password)

    #info_exibir = bootloader_exibir(session, dburi, nome_tabela, valores_exibir)
    info_filtros = bootloader_filtros(session, nome_tabela, valores_filtros)

    #return info_exibir, info_filtros
    print(info_filtros['datas'][0].texto)

if __name__ == "__main__":
    main('123', 'Avaliacao', 0, {'data':['2021-08-21', '2021-11-15']})