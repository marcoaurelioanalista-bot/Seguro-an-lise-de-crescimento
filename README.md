# 🚀 Seguro Growth Analytics
**Inteligência Comercial e Analytics aplicado ao Mercado Segurador**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-FF6F00?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)

## 📌 O Contexto de Negócio
Corretoras e Seguradoras possuem um volume gigantesco de dados operacionais, mas muitas vezes a equipe comercial trabalha "no escuro". Os principais desafios da operação são:
1. **Churn Oculto:** Clientes cancelam ou não renovam apólices, e a empresa só descobre no dia do vencimento.
2. **Dinheiro na Mesa:** Clientes com apenas um produto (ex: Auto) que possuem perfil para comprar outros (ex: Vida, Residencial), mas não recebem ofertas direcionadas (Cross-Sell).
3. **Falta de Prioridade:** Corretores gastam tempo ligando para leads frios enquanto perdem oportunidades quentes.

## 💡 A Solução
O **Seguro Growth Analytics** é um projeto de ponta a ponta que utiliza Análise de Dados e Machine Learning para transformar dados operacionais em **decisões comerciais lucrativas**. O projeto é dividido em 3 motores principais:

- 🔴 **Renewal Score (Prevenção de Churn):** Modelo de classificação (Random Forest) que prevê a probabilidade de um cliente não renovar o seguro, permitindo ação preventiva.
- 🟢 **Cross-Sell Engine (Expansão de Receita):** Algoritmo de recomendação baseado em regras de negócio para identificar o próximo "melhor produto" para a carteira ativa.
- 🟡 **Lead Prioritization (Eficiência Comercial):** Score dinâmico (0 a 100) que cruza receita potencial e probabilidade de conversão para rankear para quem o time de vendas deve ligar hoje.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Manipulação de Dados:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (Random Forest Classifier)
- **Visualização e BI:** Power BI, DAX
- **Versionamento:** Git & GitHub

## 📂 Estrutura do Projeto
```text
seguro-growth-analytics/
│
├── data/
│   ├── raw/                 # Base de dados original (gerada via script)
│   └── processed/           # Bases com scores gerados pelos modelos (.csv)
│
├── src/                     # Scripts de processamento e ML
│   ├── generate_data.py     # Script para simular o dataset de seguros
│   ├── renewal_score.py     # Modelo preditivo de probabilidade de renovação
│   ├── cross_sell.py        # Motor de oportunidades e ticket médio
│   └── lead_score.py        # Algoritmo de priorização da fila de vendas
│
├── dashboard/
│   └── seguro_growth_analytics.pbix  # Visão executiva no Power BI
│
├── README.md
└── requirements.txt
