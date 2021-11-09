# coding: utf-8
from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.orm.exc import NoResultFound
import psycopg2
from sqlalchemy.orm.exc import StaleDataError
from DAO import DAOCrud

class manipulaBanco():
    def inserirDados(comercios, usuarios):
        try:
            sessao = DAOCrud.getSession()
            for i in range(max(len(comercios), len(usuarios))):
                if i < len(comercios):
                    DAOCrud.insere(sessao, comercios[i])
                if i < len(usuarios):
                    DAOCrud.insere(sessao, usuarios[i])
            sessao.commit()
            sessao.close()
            return 1
        except psycopg2.Error as e:
            return e.pgerror

    def inserirDados2(transacoes, localizacoes, avaliacoes):
        try:
            sessao = DAOCrud.getSession()
            for i in range(max(len(transacoes), len(localizacoes))):
                if i < len(transacoes):
                    DAOCrud.insere(sessao, transacoes[i])
                if i < len(localizacoes):
                    DAOCrud.insere(sessao, localizacoes[i])
            for objeto in avaliacoes:
                DAOCrud.insere(sessao, objeto)
            sessao.commit()
            sessao.close()

            return 1
        except psycopg2.Error as e:
            return e.pgerror
