CREATE TABLE comercio(
	id varchar(22) NOT NULL,
	nome varchar(255) NOT NULL,
	fechado bool NOT NULL,
	telefone varchar(20) NOT NULL,
	preco varchar(4),
	pseudonimo varchar(255),
	titulo_categoria varchar(255) NOT NULL,
	pseudonimo_categoria varchar(255),
	quant_avaliacoes int NOT NULL,
	primary key(id)
);

CREATE TABLE usuario(
	id varchar(22) NOT NULL,
	nome varchar(255) NOT NULL,
	primary key(id)
);

CREATE TABLE avaliacao(
	id_comercio varchar(22) NOT NULL,
	id_usuario varchar(22) NOT NULL,
	id varchar(22) NOT NULL,
	nota int NOT NULL,
	texto text,
	data date NOT NULL, 
	horario time NOT NULL,
	primary key(id),
	foreign key(id_comercio) references comercio(id),
	foreign key(id_usuario) references usuario(id)
);

CREATE TABLE transacao(
	id_comercio varchar(22) NOT NULL,
	id serial NOT NULL,
	tipo varchar(255) NOT NULL,
	primary key(id),
	foreign key(id_comercio) references comercio(id)
);


CREATE TABLE localizacao(
	id_comercio varchar(22) NOT NULL,
	id serial NOT NULL,
	cod_postal varchar(20) NOT NULL,
	pais varchar(255) NOT NULL,
	estado varchar(255) NOT NULL,
	cidade varchar(255) NOT NULL,
	logradouro varchar(255) NOT NULL,
	primary key(id),
	foreign key(id_comercio) references comercio(id)
);
