CREATE TABLE comercio(
	id varchar(22),
	nome varchar(255),
	fechado bool,
	telefone varchar(20),
	preco varchar(4),
	pseudonimo varchar(255),
	titulo_categoria varchar(255),
	pseudonimo_categoria varchar(255),
	quant_avaliacoes int,
	primary key(id)
);

CREATE TABLE usuario(
	id varchar(22),
	nome varchar(255),
	primary key(id)
);

CREATE TABLE avaliacao(
	id_comercio varchar(22),
	id_usuario varchar(22),
	id varchar(22),
	nota int,
	texto text,
	data date, 
	horario time,
	primary key(id),
	foreign key(id_comercio) references comercio(id),
	foreign key(id_usuario) references usuario(id)
);

CREATE TABLE transacao(
	id_comercio varchar(22),
	id serial,
	tipo varchar(255),
	primary key(id),
	foreign key(id_comercio) references comercio(id)
);


CREATE TABLE localizacao(
	id_comercio varchar(22),
	id serial,
	cod_postal varchar(20),
	pais varchar(255),
	estado varchar(255),
	cidade varchar(255),
	logradouro varchar(255),
	primary key(id),
	foreign key(id_comercio) references comercio(id)
);
