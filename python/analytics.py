import sys 
sys.path.append(r'C:\Users\SALA443\Desktop\Projetos\josecarlos-dataengineer\Analise_de_carteira\analise_carteira_env\Lib\site-packages')
from environment import mysql_etl,mongo_etl, env_builder
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

if __name__ == "__main__":
    def consulta_mysql(query:str):
        '''
        Função que cria a conexão com mysql, checando se o host é local
        ou container.
        '''
        mydb = env_builder.client_mysql()

        mycursor = mydb.cursor()
        mycursor.execute("""select Papel, Cotação from fundamentus""")

        result = mycursor.fetchall()

        df = pd.DataFrame(result,columns=['Papel',
        'Cotação'])
        
        return df
    
    def grafico(database:str,collection:str,query:str):
        '''
        Função que apresenta em gráfico a comparação do total apresentado
        como compra na collection operacoes armazenada no MongoDB com o 
        total considerando o valor apresentado na tabela fundamentus armazenada
        no MySQL.        
        '''
    
        mongo = mongo_etl.mongo_to_dict_list(database=database,collection=collection)

        # transformando o resultado da consulta em um dataframe
        list_ = []
        for m in mongo:
            ticker = list(m.keys()).pop()
            m = list(m.values())
            qt_vl = m.pop()
            qt = str(list(qt_vl.keys())[0])
            qt_vl.values()
            vl =  str(list(qt_vl.values())[0])
            m.append(ticker)
            m.append(qt)
            m.append(vl)

            list_.append(m)
        df_mongo = pd.DataFrame(list_,columns=['id_usuario','id_carteira','id','tipo','data','ticker','quantidade','valor'])

        # definindo a consulta
        query = query

        # atribuindo ao dataframe
        df_fundamentus = consulta_mysql(query)

        # selecionando algumas colunas para analisar
        df_fundamentus = df_fundamentus[['Papel','Cotação']].reset_index()

        # Fazendo join entre os dataframes mongo e mwsql
        df_analytics = df_mongo.merge(df_fundamentus,left_on='ticker',right_on='Papel')

        # Adicionando as colunas total_compra, total_hoje e variacao
        df_analytics['total_compra'] = df_analytics['quantidade'].astype('int64') * df_analytics['valor'].astype('float64')
        df_analytics['total_hoje'] = df_analytics['quantidade'].astype('int64') * df_analytics['Cotação'].astype('float64')
        df_analytics['variacao'] = ((df_analytics['total_hoje'] / df_analytics['total_compra']) - 1) * 100

        # plotando o primeiro gráfico para comparar compra e atual
        fig = df_analytics.plot.bar(x='ticker',y=['total_compra','total_hoje'])
        
grafico(
    database='plataforma',
    collection='operacoes',
    query='select Papel, Cotação from fundamentus;')
