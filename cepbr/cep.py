# -*- coding: utf-8 -*-

#####################################################################
# CEPBR - Biblioteca consulta ao CEP pelo site dos correios do Brasil
#
# contribuição: Lucas Magnum
####################################################################

from BeautifulSoup import BeautifulSoup
import requests


class CEP():

    def __init__(self):
        self.url = 'http://m.correios.com.br/movel/buscaCepConfirma.do'
        self.result = []

    def get_cep(self, cep):

        if not cep:
            raise ValueError('É necessário infortar um CEP.')

        http_response = requests.post(
            self.url,
            data={
                'cepEntrada': cep,
                'tipoCep': '',
                'cepTemp': '',
                'metodo': 'buscarCep'
            })

        if not http_response.status_code == 200:
            raise requests.HTTPError(
                'Response code %i' % http_response.status_code)

        nodes = BeautifulSoup(http_response.text).findAll(
            'span', {'class': 'respostadestaque'})

        logradouro, bairro, cidade_uf, cep = [n.text.strip() for n in nodes]
        cidade_uf = [i.strip() for i in cidade_uf.split('\n')]
        cidade, uf = cidade_uf[0], cidade_uf[-1].replace('/', '')

        return {
            'logradouro': logradouro,
            'bairro': bairro,
            'cidade': cidade,
            'uf': uf,
            'cep': cep
        }
