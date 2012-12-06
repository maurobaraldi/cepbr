CEP-BR
======

### Biblioteca em Python para acesso à base de CEP dos Correios do Brasil

Inspirada no [postmon](https://github.com/CodingForChange/postmon), a proposta dela é ser mais simples e modular.

Aviso: CEP-BR utiliza uma url de busca dos site dos Correios do Brasil. Sua disponibilidade esta diretamente associada a
disponibilidade dessa url. Para acesso à base de dados de CEP atualizada, deve-se entrar em contato diretamente com os 
[Correios do Brasil](http://www.correios.com.br/). Infelizmente essa base de dados é paga, cara, e tem atualização trimestral. 

### Pré-requisitos

[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) - Biblioteca para scraping de HTML e XML.

[requests](docs.python-requests.org) - Biblioteca para manipulação de dados através do protocolo HTTP.

Para instalar:

```
pip install -r requirements.txt
```


### Modo de uso
```
>>> from cepbr import CEP
>>> c = CEP()
>>> c.get_cep('01154030')
{'bairro': u'Barra Funda', 'cidade': u'S\xe3o Paulo', 'uf': u'SP', 'logradouro': u'Rua Margarida', 'cep': u'01154030'}
>>> 
>>> c.get_cep('05437001')
{'bairro': u'Sumarezinho', 'cidade': u'S\xe3o Paulo', 'uf': u'SP', 'logradouro': u'Rua Heitor Penteado - de 1059 a 1769 - lado \xedmpar', 'cep': u'05437001'}
>>> 
```

### Testes
- Doctests

```
python -m doctest cep_doctest.rst -v
```

### Contribuições
[Lucas Magnum](https://github.com/LucasMagnum) (Doctests e Refactoring)

### Contato
Mauro Navarro Baraldi (mauro.baraldi@gmail.com)
[github](https://github.com/maurobaraldi) & [twitter](http://twitter.com/mauro_baraldi)


Keep Hacking in a Free World!