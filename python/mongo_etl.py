# import sys 
# sys.path.append(r'C:\Users\SALA443\Desktop\Projetos\DataEngineering_Kubernetes\test_folder\Lib\site-packages')
from environment import *

filesl = ['usuarios.json','carteiras.json','operacoes.json'] 
# path = r'C:\Users\SALA443\Desktop\Projetos\josecarlos-dataengineer\Analise_de_carteira\testes\python\\'
path = env_builder.path_scan()

database = 'plataforma'

mongo_etl.carga_mongodb_many(path=path,files=filesl,database=database)

mongo_etl.mongo_to_dict_list(database='plataforma',collection='carteiras')

mongo_etl.mongo_list_to_list_dict(database='plataforma',collections=['usuarios','carteiras','operacoes'])




        
    



