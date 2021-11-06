class Comercio():
    def __init__(self, id, nome, fechado, telefone, preco, pseudonimo, titulo_categoria, pseudonimo_categoria, quant_avaliacoes):
        self.id = id,
        self.nome = nome,
        self.fechado = fechado,
        self.telefone = telefone,
        self.preco = preco,
        self.pseudonimo = pseudonimo,
        self.titulo_categoria = titulo_categoria,
        self.pseudonimo_categoria = pseudonimo_categoria,
        self.quant_avaliacoes = quant_avaliacoes

class Localizacao():
    def __init__(self, id_comercio, cod_postal, pais, estado, cidade, logradouro):
        self.id_comercio = id_comercio,
        # É necessário ver a questão do id serial
        self.cod_postal = cod_postal,
        self.pais = pais, 
        self.estado = estado,
        self.cidade = cidade,
        self.logradouro = logradouro

class Avaliacao():
    def __init__(self, id_comercio, id_usuario, id, nota, texto, data, horario):
        self.id_comercio = id_comercio,
        self.id_usuario = id_usuario,
        self.id = id,
        self.nota = nota,
        self.texto = texto,
        self.data = data,
        self.horario = horario

class Usuario():
    def __init__(self, id, nome):
        self.id = id,
        self.nome = nome