import sys 
sys.path.append(r'C:\Users\SALA443\Desktop\Projetos\josecarlos-dataengineer\Analise_de_carteira\analise_carteira_env\Lib\site-packages')
from environment import mysql_etl,mongo_etl
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Buscando os dados das compras no mongodb
    mongo = mongo_etl.mongo_to_dict_list(database='plataforma',collection='operacoes')

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
        print(m)    
        list_.append(m)
    df_mongo = pd.DataFrame(list_,columns=['id_usuario','id_carteira','id','tipo','data','ticker','quantidade','valor'])

    # estabelecendo a conexão
    engine = mysql_etl(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'db'
    ).criar()

    # definindo a consulta
    query = "SELECT * FROM fundamentus;"

    # atribuindo ao dataframe
    df_fundamentus = pd.read_sql_query(query,engine)

    # selecionando algumas colunas para analisar
    df_fundamentus = df_fundamentus[['Papel','Cotação','data_carga']].reset_index()

    # Fazendo join entre os dataframes mongo e mwsql
    df_analytics = df_mongo.merge(df_fundamentus,left_on='ticker',right_on='Papel')

    # Adicionando as colunas total_compra, total_hoje e variacao
    df_analytics['total_compra'] = df_analytics['quantidade'].astype('int64') * df_analytics['valor'].astype('float64')
    df_analytics['total_hoje'] = df_analytics['quantidade'].astype('int64') * df_analytics['Cotação'].astype('float64')
    df_analytics['variacao'] = ((df_analytics['total_hoje'] / df_analytics['total_compra']) - 1) * 100

    # plotando o primeiro gráfico para comparar compra e atual
    fig = df_analytics.plot.bar(x='ticker',y=['total_compra','total_hoje'])
