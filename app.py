# app.py
import streamlit as st
import pandas as pd

st.title("Dashboard Portfolio")

# Leitura de dados (substitua isso pelo código que lê seus dados)
data = {
    'Produto': ['Financeiro as a Service', 'Financeiro as a Service', 'CFO as a Service', 'CFO as a Service'],
    'Projeto': ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4'],
    'Cliente': ['Biologix', 'DrJB', 'Histeria!', 'Total Produto'],
    'Vendas': [1000, 0, 500, 1500],
    'Receita': [500, 200, 300, 1000],
    'Margem$': [150, 110, 130, 390],
    'Margem%': [30, 55, 43, 39],
    'Vendas/Receita': [2, 0, 1.67, 1.5],
    'Vendas YoY Growth': [200, -100, 75, 75],
    'Receita YoY Growth': [-30, 10, 10, 10],
    'Margem YoY Growth': [-40, 16, 12, 12],
}

df = pd.DataFrame(data)

# Exibir dados tabulares
st.write("Dados:")
st.dataframe(df)

# Gráficos
st.write("Gráfico de Vendas:")
st.bar_chart(df['Vendas'])

st.write("Gráfico de Receita:")
st.bar_chart(df['Receita'])
