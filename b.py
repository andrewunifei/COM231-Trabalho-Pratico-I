# coding: utf-8
from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import StaleDataError
from mapeamento import OrderDetail
from DAO import DAOCrud
from DAO import DAOVendas

class manipulaBanco():
    def inserirDados(comercios, localizacoes, avaliacoes, usuarios, transacoes):
        try:
            sessao = DAOCrud.getSession()

            for i in range(max(len(comercios), len(localizacoes), len(avaliacoes), len(usuarios), len(transacoes))):
                if i < len(comercios):
                    DAOCrud.insere(sessao, comercios[i])
                if i < len(localizacoes):
                    