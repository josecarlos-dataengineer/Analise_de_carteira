# Append do caminho do venv python ***desnecessário quando executado em container***
# import sys 
# sys.path.append(r'C:\Users\SALA443\Desktop\Projetos\josecarlos-dataengineer\Analise_de_carteira\analise_carteira_env\Lib\site-packages')

# importação dos módulos
from environment import api_get,mysql_etl

# Chamada das funções
if __name__ == "__main__":
    # Cria dataframe com dados atuais de cada função, coletando do site fundamentus
    df = api_get(
        url='https://www.fundamentus.com.br/resultado.php',
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}).fundamentus_df()

    # Tratamento dos campos numéricos mencionados na lista
    collist = ['Cotação','P/L','P/VP','PSR','Div.Yield','P/Ativo','P/Cap.Giro','P/EBIT','P/Ativ Circ.Liq','EV/EBIT','EV/EBITDA','Mrg Ebit','Mrg. Líq.','Liq. Corr.','ROIC','ROE','Liq.2meses','Patrim. Líq','Dív.Brut/ Patrim.','Cresc. Rec.5a']
    for c in collist:   
        exec(f"df['{c}'] = api_get.data_cleaning(df['{c}'])")
    
    # Conecta engine ***Atenção para o host*** ver docstring da classe mysql_etl
    engine = mysql_etl(
        host = 'host.docker.internal',
        user = 'root',
        password = 'root',
        database = 'db'
    ).criar()
    # # Carrega os dados tratados no banco Mysql
    df.to_sql('fundamentus', con=engine, if_exists='replace', index=False)