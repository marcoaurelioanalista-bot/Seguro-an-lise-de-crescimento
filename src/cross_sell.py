import pandas as pd

def gerar_oportunidades_cross_sell(caminho_clientes, caminho_apolices):
    """
    Identifica oportunidades de Cross-Sell baseado na carteira atual.
    """
    clientes = pd.read_csv(caminho_clientes)
    apolices = pd.read_csv(caminho_apolices)
    
    df = pd.merge(clientes, apolices, on='id_cliente')
    
    oportunidades = []
    
    for index, row in df.iterrows():
        produtos_atuais = str(row['produtos_ativos']).split(',')
        
        if 'Auto' in produtos_atuais and 'Residencial' not in produtos_atuais:
            oportunidades.append({
                'id_cliente': row['id_cliente'],
                'produto_recomendado': 'Seguro Residencial',
                'receita_potencial': 650.00,
                'probabilidade_aceitacao': 0.65
            })
            
        if 'Auto' in produtos_atuais and 'Vida' not in produtos_atuais and row['idade'] > 30:
            oportunidades.append({
                'id_cliente': row['id_cliente'],
                'produto_recomendado': 'Seguro de Vida',
                'receita_potencial': 720.00,
                'probabilidade_aceitacao': 0.55
            })
            
    df_oportunidades = pd.DataFrame(oportunidades)
    df_oportunidades.to_csv('data/processed/cross_sell_opportunities.csv', index=False)
    print(f"{len(df_oportunidades)} oportunidades de Cross-Sell identificadas.")

if __name__ == "__main__":
    gerar_oportunidades_cross_sell('data/raw/clientes.csv', 'data/raw/apolices.csv')
