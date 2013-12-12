# -*- coding: utf-8 -*-

#####################################################################
# CEPBR - Biblioteca consulta ao CEP pelo site dos correios do Brasil
#
# v1.0
# - Puramente em Python. Somente bibliotecas da standard lib.
# - Código otimizado.
# - Resultado em JSON.
####################################################################

import json
import urllib

class CEP():

    def __init__(self):
        self.url = 'http://cep.correiocontrol.com.br/%s.json'

    def get_cep(self, cep):
        if not cep:
            raise ValueError('É necessário informar um CEP.')        

        try:
            query = urllib.urlopen(self.url % cep).read()
            return json.loads(query)
        except ValueError:
            raise ValueError('CEP inválido ou incompleto.')
        except IOError:
            raise IOError('Não foi possível encontrar o CEP. Verifique sua conexão.')    
