from sqlalchemy import MetaData

# Função para consultar o tamanho em bytes de uma tabela e/ou do banco todo
def table_sizes(table_name, wholedb=False):

    dburi = "postgresql+psycopg2://postgres:root@localhost:5432/yelp"

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
    
    return t

# if __name__ == "__main__":