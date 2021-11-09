# Para rodar o requisito.txt: pip install -r requisito.txt 

# -*- coding: utf-8 -*-
"""
Yelp Fusion API code sample.
This program demonstrates the capability of the Yelp Fusion API
by using the Search API to query for businesses by a search term and location,
and the Business API to query additional information about the top result
from the search query.
Please refer to http://www.yelp.com/developers/v3/documentation for the API
documentation.
This program requires the Python requests library, which you can install via:
`pip install -r requirements.txt`.
Sample usage of the program:
`python sample.py --term="bars" --location="San Francisco, CA"`
"""
from __future__ import print_function

import argparse
import json
import pprint
import requests
import sys
import urllib
import mapeamento as tabela


# This client code can run on Python 2.x or 3.x.  Your imports can be
# simpler if you only need one of those.
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode


# Yelp Fusion no longer uses OAuth as of December 7, 2017.
# You no longer need to provide Client ID to fetch Data
# It now uses private keys to authenticate requests (API Key)
# You can find it on
# https://www.yelp.com/developers/v3/manage_app
API_KEY="jP_sZ5s35vlKdCW0Pa-85OSQg-O-1PGHJUPbyM4y_bjpxrLEJmr4kzLtpHTzLRaWZ79n3NPOMUUrmB2Qq3oQ3Cn_RsMktpBDB1ipnDAgskGaI4iSmYmx80ewhLqFYXYx" 


# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
REVIEW_PATH = '/v3/businesses/{0}/reviews' # Para consultar as avaliações


# Defaults for our simple example.
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 20

def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(api_key, location, offset):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """
    url_params = {
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'offset': offset
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)

def get_review(api_key, business_id):
    review_path = REVIEW_PATH.format(business_id)

    return request(API_HOST, review_path, api_key)


def query_api(location):
    # O offset são blocos de respostas
    # Se offset = 0 então os SEARCH_LIMIT primeiros registros são retornados
    # Se offset = 20 então os SEARCH_LIMIT + (deslocamento de 20 registros) são retornados
    # Isso é necessário porque a API retorna apenas SEARCH_LIMIT registros por vez
    # No nosso caso SEARCH_LIMIT = 20
    # O valor de offset é incrementado em 20 a cada nova requisição
    offset = 0
    index = 0

    comercios = list()
    localizacoes = list()
    avaliacoes = list()
    usuarios = list()
    transacoes = list()
    
    response = search(API_KEY, location, offset)
    total_businesses = response.get('total')

    # Passagem dos atributos relevantes do objeto JSON
    # São necessárias várias requisições, porque a API retorna no máximo 50 objetos
    # No nosso caso vamos retornar 20 objetos a cada requisição
    if(total_businesses == 240):
        number_of_request = response.get('total')/SEARCH_LIMIT # 240/20

        for request in range(1):
            response = search(API_KEY, location, offset)
            businesses = response.get('businesses')

            if not businesses:
                print(u'No businesses in {1} found.'.format(location))
                return

            for business in businesses:
                response_comercio = get_business(API_KEY, business['id'])
                response_avaliacao = get_review(API_KEY, business['id'])

                try:
                    comercios.append(
                        tabela.Comercio(
                            id = response_comercio["id"],
                            nome = response_comercio["name"],
                            fechado = response_comercio["is_closed"],
                            telefone = response_comercio["phone"],
                            preco = response_comercio["price"],
                            pseudonimo = response_comercio["alias"],
                            titulo_categoria = response_comercio["categories"][0]["title"],
                            pseudonimo_categoria = response_comercio["categories"][0]["alias"],
                            quant_avaliacoes = response_comercio["review_count"]
                        )
                    )               

                except KeyError as e:
                    comercios.append(
                        tabela.Comercio(
                            id = response_comercio["id"],
                            nome = response_comercio["name"],
                            fechado = response_comercio["is_closed"],
                            telefone = response_comercio["phone"],
                            preco = None,
                            pseudonimo = response_comercio["alias"],
                            titulo_categoria = response_comercio["categories"][0]["title"],
                            pseudonimo_categoria = response_comercio["categories"][0]["alias"],
                            quant_avaliacoes = response_comercio["review_count"]
                        )
                    )

                for type in response_comercio["transactions"]:
                    transacoes.append(
                        tabela.Transacao(
                            id_comercio = response_comercio["id"],
                            tipo = type
                        )
                    )

                localizacoes.append(
                    tabela.Localizacao(
                        id_comercio = response_comercio["id"],
                        # É necessário ver a questão do id serial
                        cod_postal = response_comercio["location"]["zip_code"],
                        pais = response_comercio["location"]["country"],
                        estado = response_comercio["location"]["state"],
                        cidade = response_comercio["location"]["city"],
                        logradouro = response_comercio["location"]["address1"]
                    )
                )

                for avaliacao in response_avaliacao["reviews"]:
                    avaliacoes.append(
                        tabela.Avaliacao(
                            id_comercio = response_comercio["id"],
                            id_usuario = avaliacao["user"]["id"],
                            id = avaliacao["id"],
                            nota = avaliacao["rating"],
                            texto = avaliacao["text"],
                            data = avaliacao["time_created"].split()[0],
                            horario = avaliacao["time_created"].split()[1]
                        )
                    )

                usuarios.append(
                    tabela.Usuario(
                        id = avaliacao["user"]["id"],
                        nome = avaliacao["user"]["name"]
                    )
                )                    

            offset = offset + 20
    
    else:
        print("A API encontrou mais de 240 casos, precisamos tratar esse cenário")
    
    return comercios, transacoes, localizacoes, avaliacoes, usuarios


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    try:
        comercios, transacoes, localizacoes, avaliacoes, usuarios = query_api(input_values.location)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )
    return comercios, usuarios, transacoes, localizacoes, avaliacoes

#if __name__ == '__main__':
#    main()
