import requests
import os

def get_active_cluster_or_first(clusters, databricks_host, databricks_token):
    """
    Verifica se há clusters ativos e retorna o ID do cluster ativo.
    Caso nenhum esteja ativo, retorna o ID do primeiro cluster da lista.

    Args:
        clusters (dict): Dicionário de clusters no formato {ID: Nome}.
        databricks_host (str): URL do Databricks.
        databricks_token (str): Token de autenticação para a API do Databricks.

    Returns:
        str: ID do cluster ativo ou do primeiro cluster na lista.
    """
    headers = {
        "Authorization": f"Bearer {databricks_token}",
        "Content-Type": "application/json"
    }

    # Verifica o estado de todos os clusters
    response = requests.get(f"{databricks_host}/api/2.0/clusters/list", headers=headers)
    if response.status_code != 200:
        raise Exception(f"Erro ao listar clusters: {response.text}")
    
    clusters_data = response.json().get("clusters", [])
    
    # # Verifica se há clusters ativos na lista
    # for cluster in clusters_data:
    #     if cluster["cluster_id"] in clusters and cluster["state"] == "RUNNING":
    #         return cluster["cluster_id"]  # Retorna o ID do cluster ativo
        
    # Percorre a lista na ordem definida na variável 'clusters'
    for cluster_id in clusters.keys():
        for cluster in clusters_data:
            if cluster["cluster_id"] == cluster_id and cluster["state"] == "RUNNING":
                return cluster_id  # Retorna o ID do cluster ativo na ordem da variável 'clusters'

    # Nenhum cluster está ativo, retorna o ID do primeiro cluster
    return list(clusters.keys())[0]