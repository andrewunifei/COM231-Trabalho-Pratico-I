from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mapeamento import *

def getTable(nome_tabela):
    if nome_tabela == "Comercio": return Comercio
    elif nome_tabela == "Usuario": return Usuario
    elif nome_tabela == "Avaliacao": return Avaliacao
    elif nome_tabela == "Localizacao": return Localizacao
    else: return Transacao

def dbCount(session):
    tables = [Comercio, Usuario, Avaliacao, Localizacao, Transacao]
    total = int()

    for table in tables:
        total += session.query(table).count()
    
    return total

def tableCount(table, session):
    # Função para retornar o número total de registros em uma tabela
    return session.query(table).count()


def tableSize(dburi, nome_tabela, wholedb):
    # Função para consultar o tamanho em bytes de uma tabela e/ou do banco todo

    t = dict()
    m = MetaData(dburi)
    e = lambda x: m.bind.execute(x).first()[0] # Função anonima que executa a query
    m.reflect()
    q_pretty_size = "SELECT pg_size_pretty(pg_total_relation_size('%s'))"
    q_pretty_total = "SELECT pg_size_pretty(pg_database_size('yelp'))"

    # A função pretty retorna o tamanho como "human-readable"
    t['size'] = e(q_pretty_size % nome_tabela) # Une a string ao nome_tabela

    if wholedb:
        t['total'] = e(q_pretty_total)
    else:
        t['total'] = None
    
    return t

def bootloader_exibir(session, dburi, nome_tabela, valores_exibir):
    info = {}
    
    if valores_exibir[0]: info['tableCount'] = tableCount(getTable(nome_tabela), session)
    else: info['tableCount'] = None

    if valores_exibir[1]: info['dbCount'] = dbCount(session)
    else: info['dbCount'] = None

    if valores_exibir[2]: info['tableSize'] = tableSize(dburi, nome_tabela, valores_exibir[3])
    else: info['tableSize'] = None

    session.close()

    return info