from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mapeamento import *

def getTable(table_name):
    if table_name == "Comercio": return Comercio
    elif table_name == "Usuario": return Usuario
    elif table_name == "Avaliacao": return Avaliacao
    elif table_name == "Localizacao": return Localizacao
    else: return Transacao

def dbCount(session):
    tables = [Comercio, Usuario, Avaliacao, Localizacao]
    total = int()

    for table in tables:
        total += session.query(table).count()
    
    return total

def tableCount(table, session):
    # Função para retornar o número total de registros em uma tabela
    return session.query(table).count()


def tableSize(table_name, wholedb):
    # Função para consultar o tamanho em bytes de uma tabela e/ou do banco todo

    dburi = "postgresql+psycopg2://postgres:123@localhost:5432/yelp"

    t = dict()
    m = MetaData(dburi)
    e = lambda x: m.bind.execute(x).first()[0] # Função anonima que executa a query como um metadado
    m.reflect()
    q_pretty_size = "SELECT pg_size_pretty(pg_total_relation_size('%s'))"
    q_pretty_total = "SELECT pg_size_pretty(pg_database_size('yelp'))"

    # A função pretty retorna o tamanho como "human-readable"
    t['size'] = e(q_pretty_size % table_name) # Une a string ao table_name

    if wholedb:
        t['total'] = e(q_pretty_total)
    else:
        t['total'] = None
    
    return t

def bootloader(table_name, criterios):
    engine = create_engine("postgresql+psycopg2://postgres:123@localhost:5432/yelp", echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    info = {}
    
    if criterios[0]: info['tableCount'] = tableCount(getTable(table_name), session)
    else: info['tableCount'] = None

    if criterios[1]: info['dbCount'] = dbCount(session)
    else: info['dbCount'] = None

    if criterios[2]: info['tableSize'] = tableSize(table_name, criterios[3])
    else: info['tableSize'] = None

    session.close()

    return info

if __name__ == "__main__":
    bootloader()