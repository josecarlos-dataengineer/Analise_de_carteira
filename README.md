# Analise_de_carteira
Neste repositório, estou desenvolvendo um processo de análise de carteiras. A ideia é tratar arquivos json, contendo carteiras de investimento, usuarios e perfis de investimento. Esses arquivos são armazenados em banco NOSQL, e posteriormente tratados para que seja feita a análise da evolução dessas carteiras de investimento. 
Para acompanhar a evolução dos preços das ações, será feita extração diária, e o armazenamento será feito em banco de dados relacional. 
A plotagem dos dados será feita pelo uso da biblioteca Plotly.

# Tecnologias usadas:
* Mongodb
* Docker
* SQL
* Python

## Status do projeto:
* Docker Python: Feito
* Docker Mongo: Feito
* Docker Compose: Feito
* Python (criação dos documentos): Feito
* Pymongo (ETL para o Mongo): Feito
* Docker MySQL: Pendente
* Python (ETL para o MySQL): Pendente
* Plotly

## Processo de carga no Mongodb:
O processo de carga dos documentos dentro das collections é feito conforme a seguir:

***Após clonar o repositório:***
docker-compose up (Este comando fará a construção das imagens Mongodb, Python e MySQL)

docker run --name pythonapp  -it  test-python-app bash

***Abra um terminal e insira o comando abaixo:*** <br>
* docker exec -it <mongo container> bash

***Abra outro terminal e insira o comando abaixo:***
* docker run -it --name pythonapp test-python-app

***Em um outro terminal, digite os comandos abaixo:***
* mongosh
* show dbs
![alt text](imagens/show_dbs.png)  <br>

* use <banco de dados>  <br>
* db.<collection>.find()  <br>
![alt text](imagens/collection_find.png)  <br>



