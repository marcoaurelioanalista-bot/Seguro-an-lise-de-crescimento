import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def treinar_modelo_renewal(caminho_dados):
    """
    Treina um modelo para prever o risco de não renovação da apólice.
    """
    print("Carregando dados de apólices e clientes...")
    df = pd.read_csv(caminho_dados)
    
    features = ['idade', 'tempo_relacionamento_anos', 'sinistros_ultimos_12m', 
                'atrasos_pagamento', 'valor_premio']
    
    X = df[features].fillna(0)
    y = df['renovou_historico']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    print("Treinando modelo Random Forest...")
    modelo = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
    modelo.fit(X_train, y_train)
    
    df['probabilidade_renovacao'] = modelo.predict_proba(X)[:, 1]
    
    condicoes = [
        (df['probabilidade_renovacao'] >= 0.80),
        (df['probabilidade_renovacao'] >= 0.50) & (df['probabilidade_renovacao'] < 0.80),
        (df['probabilidade_renovacao'] < 0.50)
    ]
    classificacoes = ['Baixo Risco', 'Médio Risco', 'Alto Risco']
    df['faixa_risco'] = np.select(condicoes, classificacoes)
    
    df.to_csv('data/processed/renewal_scored.csv', index=False)
    print("Base de Renewal Score gerada com sucesso!")

if __name__ == "__main__":
    treinar_modelo_renewal('data/raw/dataset_seguros.csv')
