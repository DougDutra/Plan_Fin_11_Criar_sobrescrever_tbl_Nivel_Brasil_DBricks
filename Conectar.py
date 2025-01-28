print("\n\n############### Planejamento Financeiro ###############\n")
print("Desenvolvedor do Script: Douglas Dutra")
print("Contato: (11) 97569-7222")
print("Criado em: 28/01/2025")
print("Objetivo: Ler uma base local e criar/sobrescrever uma tabela direto no Databricks \n")

from dotenv import load_dotenv
import os
import pandas as pd
from Funcoes.crud_dbricks import criar_sobrescrever_tbl
from Funcoes.verificar_cluster import get_active_cluster_or_first
from databricks.connect import DatabricksSession

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#========================================= CONFIGURAÇÕES INICIAIS =========================================
# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Verificar se as variáveis foram carregadas corretamente
spark_home = os.getenv("SPARK_HOME")
databricks_host = os.getenv("DATABRICKS_HOST")
databricks_token = os.getenv("DATABRICKS_TOKEN")
databricks_cluster_01 = os.getenv("DATABRICKS_CLUSTER_ID_01")
databricks_cluster_02 = os.getenv("DATABRICKS_CLUSTER_ID_02")
databricks_cluster_03 = os.getenv("DATABRICKS_CLUSTER_ID_03")
databricks_cluster_04 = os.getenv("DATABRICKS_CLUSTER_ID_04")
databricks_cluster_05 = os.getenv("DATABRICKS_CLUSTER_ID_05")
databricks_cluster_06 = os.getenv("DATABRICKS_CLUSTER_ID_06")
databricks_cluster_07 = os.getenv("DATABRICKS_CLUSTER_ID_07")

# Validação das variáveis
if not all([spark_home, databricks_host, databricks_token]):
    raise ValueError("Uma ou mais variáveis de ambiente não foram carregadas corretamente.")
    
clusters = {
    databricks_cluster_01:"cluster_databox_logistica_malha",
    databricks_cluster_02:"cluster_databox_workflows_logistica_malha",
    databricks_cluster_03:"cluster_databox_workflows_logistica",
    databricks_cluster_04:"cluster_databox_workflows_plan_comercial",
    databricks_cluster_05:"cluster_databox_marketplace",
    databricks_cluster_06 :"cluster_databox_logistica",
    databricks_cluster_07:"cluster_databox_plan_comercial"
}

databricks_cluster = get_active_cluster_or_first(clusters, databricks_host, databricks_token)

print(f" > SPARK_HOME: {spark_home}")
print(f" > DATABRICKS_HOST: {databricks_host}")
print(f" > DATABRICKS_CLUSTER_ID: {databricks_cluster} - '{clusters[databricks_cluster]}'\n")

# Definir as variáveis de ambiente (caso necessário)
os.environ["SPARK_HOME"] = spark_home
os.environ["DATABRICKS_HOST"] = databricks_host
os.environ["DATABRICKS_TOKEN"] = databricks_token
os.environ["DATABRICKS_CLUSTER_ID"] = databricks_cluster

# Criar uma sessão Spark para conexão ao Databricks
spark = DatabricksSession.builder.getOrCreate()
#==========================================================================================================

pastaAtual = os.path.dirname(__file__)
pastaAnterior = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

df = pd.read_csv(pastaAnterior + "/tt.csv")

spark_df = spark.createDataFrame(df)
table_name = "databox.logistica_malha_estrategico.tt"

# Executar uma consulta simples para verificar a conexão
try:
    print(f" - Criando/Sobrescrevendo Tabela: '{table_name}'...")
    criar_sobrescrever_tbl(spark_df, table_name)
    print(" - Tabela criada/sobrescrita com Sucesso")

except Exception as e:
    print(f" - Erro ao Criar/Sobrescrever Tabela: {e}")

finally:
    spark.stop()
    print(" - Sessão Spark finalizada.")
