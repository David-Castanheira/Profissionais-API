# Sobre o Projeto
Criação de um dicionário simples de profissionais de uma empresa. Seus atributos incluem o ID (código único de identificação), nome e especialidade (desenvolvedor, analista, social media, gestor de tráfego, devops, entre outros...)

## Objetivo
Criação de rotas básicas em Flask, utilizando-se os verbos HTTP para manipulação do dicionário. São eles: GET (recupera os dados do dicionário), POST (cria registros no dicionário), PUT (altera registros no dicionário) e DELETE (apaga os registros do dicionário. OBS: No caso, apaga o profissional, através de seu ID).

Ajuste: A rota "PUT" não foi criada, por conta de seu mal funcionamento durante os testes. Existem algumas definições diferentes que foram usadas como teste e se encontram comentadas no arquivo em questão. Com isso, está sendo estudado uma forma para permitir a alteração de dados no dicionário de maneira correta.

## Ferramentas
Para a resolução desses exercícios, foi-se necessário a instalação de duas importantes ferramentas para consumo de API's em Python, sendo a primeira delas o framework **[Flask](https://flask.palletsprojects.com/en/3.0.x/)** para definição de rotas HTTP:

```
$ pip install Flask 
```
Para verificar se a instalação foi feita corretamente, basta rodar os comandos abaixo no terminal:

```
$ pip show Flask 
```
Ou então:
```
$ pip3 show Flask
import Flask
```

E a biblioteca **[requests](https://requests.readthedocs.io/en/latest/)** que, por sua vez, permite a realização de requisições e solicitações, estabelecendo a comunicação com outras aplicações/serviços.

```
$ pip install requests
```

Depois disso, importe ambos nos arquivos em que a utilização destes será necessária, assim como definido abaixo:

`from flask import Flask`

`from flask import request`