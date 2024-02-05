import sys 
sys.path.append(r'C:\Users\SALA443\Desktop\Projetos\DataEngineering_Kubernetes\test_folder\Lib\site-packages')

import json
import datetime
from datetime import date
import pandas as pd
import uuid
import os

# definindo os documentos de aporte e vendas
class operacao():
    '''
    operacao(id_usuario='156',id_carteira='51561',ticker='bbdc4',qtde=50,preco=38.6,operacao='venda').criar_json()       


    '''
    
    def __init__(self,id_usuario,id_carteira,ticker:str,qtde:int,preco:float,operacao:str):

        self.id_usuario = id_usuario
        self.id_carteira = id_carteira
        self.ticker = ticker
        self.qtde = qtde
        self.preco = preco
        self.operacao = operacao
    
    def criar_dict(self):
        
        document = {
            'id_usuario':self.id_usuario,
            'id_carteira':self.id_carteira,
            'id':uuid.uuid4().hex[:8],
            'tipo':self.operacao,
            'data':str(datetime.date.today()),
            self.ticker:{self.qtde:self.preco}}
        return document
    
    def criar_json(self) -> dict:    
            
        json_file = operacao(self.id_usuario,self.id_carteira,self.ticker,self.qtde,self.preco,self.operacao).criar_dict()
        # json_file = json.dumps(json_file) 
        # print(json_file)
        
        if os.path.isfile('operacoes.json') == False:
            with open('operacoes.json', 'w', encoding='utf-8') as arquivo:
                arquivo.write("[]")
                
        with open("operacoes.json", 'r') as arquivo:
            data = json.load(arquivo)            
            data.append(json_file)
            
        with open("operacoes.json", mode='w', encoding='utf-8') as arquivo:
            json.dump(data, arquivo,indent=4)
            



# Definiçao de documento Carteiras
class carteiras():
    def __init__(self,nome:str,perfil:list,tags:list,ticker:{}):
        self.nome = nome
        self.perfil = perfil
        self.tags = tags
        self.ticker = ticker

        
      
    def criar_dict(self) -> dict:
        if self.tags == None:
            self.tags = ['padrao']
        if self.perfil == None:
            self.perfil = ['padrao']
             
        document = {
            'id':uuid.uuid4().hex[:8],
            'nome':self.nome,
            'perfil':self.perfil,
            'tags':self.tags,
            'tickers':self.ticker
            
         }
        
        return document
    
    def criar_json(self) -> dict:    
            
        json_file = carteiras(self.nome,self.perfil,self.tags,self.ticker).criar_dict()         
        # json_file = json.dumps(json_file,indent=2)  
        
        if os.path.isfile('carteiras.json') == False:
            with open('carteiras.json', 'w', encoding='utf-8') as arquivo:
                arquivo.write("[]")
                
        with open("carteiras.json", 'r+',encoding='UTF-8') as arquivo:
            data = json.load(arquivo)            
            data.append(json_file)
            
        with open("carteiras.json", "w") as arquivo:
            json.dump(data, arquivo,indent=4)
            



# definindo documento usuario
class usuario():
    '''
    operacao(id_usuario='156',id_carteira='51561',ticker='bbdc4',qtde=50,preco=38.6,operacao='venda').criar_json()       
    '''
    
    def __init__(self,nome,perfis:[],carteiras:[]):


        self.nome = nome
        self.perfis = perfis
        self.carteiras = carteiras
    
    def criar_dict(self):
        
        document = {
            'id_usuario':uuid.uuid4().hex[:8],
            'nome':self.nome,
            'perfis':self.perfis,
            'carteiras':self.carteiras
        }

        return document
    
    def criar_json(self) -> dict:    
            
        json_file = usuario(self.nome,self.perfis,self.carteiras).criar_dict()
        
        if os.path.isfile('usuarios.json') == False:
            with open('usuarios.json', 'w', encoding='utf-8') as arquivo:
                arquivo.write("[]")
            
        with open("usuarios.json", 'r+',encoding='UTF-8') as arquivo:
            data = json.load(arquivo)            
            data.append(json_file)
            # json.dump(data, arquivo,indent=4)
          

        with open("usuarios.json", mode='w', encoding='UTF-8') as arquivo:
            json.dump(data, arquivo,indent=4)


# chamada das funções
usuario(nome='Icaro Onofre',perfis=['moderado','conservador'],carteiras=['governo']).criar_json()

operacao(id_usuario='21924e5c',id_carteira='43b82e2b',ticker='elet3',qtde=55,preco=40.81,operacao='compra').criar_json()  

carteiras(nome='papel',perfil=['conservador'],tags=['privadas'],ticker={'klbn4':{500:4.27}}).criar_json()
    







