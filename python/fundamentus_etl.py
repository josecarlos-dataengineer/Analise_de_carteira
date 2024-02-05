import sys 
sys.path.append(r'C:\Users\SALA443\Desktop\Projetos\josecarlos-dataengineer\Analise_de_carteira\analise_carteira_env\Lib\site-packages')

from enviroment import api_get,mysql_etl

# Cria dataframe com dados atuais de cada função, coletando do site fundamentus
df = api_get(
    url='https://www.fundamentus.com.br/resultado.php',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}).fundamentus_df()

engine = mysql_etl(
    host = 'host.docker.internal',
    user = 'root',
    password = 'root',
    database = 'db'
).criar()
# Use the engine directly for to_sql
df.to_sql('fundamentus', con=engine, if_exists='replace', index=False)




# # MySQL parametros da conexão com Mysql
# host = 'mysql'
# user = 'root'
# password = 'root'
# database = 'db'

# # Criação da conexão usando pymysql
# connection = pymysql.connect(host=host, user=user, password=password, database=database)

# # Criação da engine sqlalchemy
# engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# # Use the engine directly for to_sql
# df.to_sql('fundamentus', con=engine, if_exists='replace', index=False)

# # Fecha a conexão
# connection.close()