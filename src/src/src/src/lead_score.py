import pandas as pd

def calcular_lead_score(caminho_cross_sell, caminho_clientes):
    """
    Calcula um score (0 a 100) para priorizar a abordagem comercial.
    """
    cross = pd.read_csv(caminho_cross_sell)
    clientes = pd.read_csv(caminho_clientes)
    
    df = pd.merge(cross, clientes, on='id_cliente')
    
    max_receita = df['receita_potencial'].max()
    
    df['score_prioridade'] = (
        ((df['receita_potencial'] / max_receita) * 40) + 
        (df['probabilidade_aceitacao'] * 40) + 
        ((df['tempo_relacionamento_anos'] / 10) * 20)
    ).round(0)
    
    df['score_prioridade'] = df['score_prioridade'].apply(lambda x: 100 if x > 100 else x)
    df = df.sort_values(by='score_prioridade', ascending=False)
    
    df.to_csv('data/processed/lead_scoring.csv', index=False)
    print("Lead Score calculado e priorizado.")

if __name__ == "__main__":
    calcular_lead_score('data/processed/cross_sell_opportunities.csv', 'data/raw/clientes.csv')
