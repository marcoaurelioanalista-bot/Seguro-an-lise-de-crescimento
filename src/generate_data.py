import pandas as pd
import numpy as np
import random
import os

def gerar_dados_seguradora(num_clientes=5000):
    print("Gerando base de dados simulada de clientes e apólices...")
    
    np.random.seed(42)
    
    # 1. Gerando Clientes
    clientes_ids = range(1, num_clientes + 1)
    idades = np.random.randint(18, 75, num_clientes)
    tempo_relacionamento = np.random.randint(1, 15, num_clientes)
    
    produtos_possiveis = ['Auto', 'Auto,Residencial', 'Auto,Vida', 'Residencial', 'Vida', 'Auto,Residencial,Vida']
    produtos_ativos = np.random.choice(produtos_possiveis, num_clientes, p=[0.5, 0.15, 0.15, 0.1, 0.05, 0.05])
    
    clientes_df = pd.DataFrame({
        'id_cliente': clientes_ids,
        'idade': idades,
        'tempo_relacionamento_anos': tempo_relacionamento,
        'produtos_ativos': produtos_ativos
    })
    
    # 2. Gerando Apólices
    sinistros = np.random.choice([0, 1, 2, 3], num_clientes, p=[0.7, 0.2, 0.08, 0.02])
    atrasos = np.random.choice([0, 1, 2, 3, 4], num_clientes, p=[0.6, 0.2, 0.1, 0.05, 0.05])
    valor_premio = np.random.uniform(800, 5500, num_clientes).round(2)
    
    renovou = []
    for i in range(num_clientes):
        chance = 80 - (sinistros[i] * 15) - (atrasos[i] * 10) + (tempo_relacionamento[i] * 2)
        if chance > np.random.randint(0, 100):
            renovou.append(1)
        else:
            renovou.append(0)
            
    apolices_df = pd.DataFrame({
        'id_cliente': clientes_ids,
        'sinistros_ultimos_12m': sinistros,
        'atrasos_pagamento': atrasos,
        'valor_premio': valor_premio,
        'renovou_historico': renovou,
        'status': ['Renovado' if r == 1 else 'Cancelado' for r in renovou]
    })
    
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    
    clientes_df.to_csv('data/raw/clientes.csv', index=False)
    apolices_df.to_csv('data/raw/apolices.csv', index=False)
    
    dataset_completo = pd.merge(clientes_df, apolices_df, on='id_cliente')
    dataset_completo.to_csv('data/raw/dataset_seguros.csv', index=False)
    
    print(f"Sucesso! {num_clientes} registros gerados na pasta 'data/raw/'.")

if __name__ == "__main__":
    gerar_dados_seguradora()
