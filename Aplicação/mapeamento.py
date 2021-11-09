# coding: utf-8
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, Text, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Comercio(Base):
    __tablename__ = 'comercio'
    __table_args__ = {'schema': 'public'}

    id = Column(String(22), primary_key=True)
    nome = Column(String(255), nullable=False)
    fechado = Column(Boolean, nullable=False)
    telefone = Column(String(20), nullable=False)
    preco = Column(String(4), nullable=False)
    pseudonimo = Column(String(255))
    titulo_categoria = Column(String(255), nullable=False)
    pseudonimo_categoria = Column(String(255))
    quant_avaliacoes = Column(Integer, nullable=False)


class Usuario(Base):
    __tablename__ = 'usuario'
    __table_args__ = {'schema': 'public'}

    id = Column(String(22), primary_key=True)
    nome = Column(String(255), nullable=False)


class Avaliacao(Base):
    __tablename__ = 'avaliacao'
    __table_args__ = {'schema': 'public'}

    id_comercio = Column(ForeignKey('public.comercio.id'), nullable=False)
    id_usuario = Column(ForeignKey('public.usuario.id'), nullable=False)
    id = Column(String(22), primary_key=True)
    nota = Column(Integer, nullable=False)
    texto = Column(Text)
    data = Column(Date, nullable=False)
    horario = Column(Time, nullable=False)

    comercio = relationship('Comercio')
    usuario = relationship('Usuario')


class Localizacao(Base):
    __tablename__ = 'localizacao'
    __table_args__ = {'schema': 'public'}

    id_comercio = Column(ForeignKey('public.comercio.id'), nullable=False)
    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".localizacao_id_seq'::regclass)"))
    cod_postal = Column(String(20), nullable=False)
    pais = Column(String(255), nullable=False)
    estado = Column(String(255), nullable=False)
    cidade = Column(String(255), nullable=False)
    logradouro = Column(String(255), nullable=False)

    comercio = relationship('Comercio')


class Transacao(Base):
    __tablename__ = 'transacao'
    __table_args__ = {'schema': 'public'}

    id_comercio = Column(ForeignKey('public.comercio.id'), nullable=False)
    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".transacao_id_seq'::regclass)"))
    tipo = Column(String(255), nullable=False)

    comercio = relationship('Comercio')