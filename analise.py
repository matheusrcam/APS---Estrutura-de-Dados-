import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def bubble_sort(lista, chave):
    n = len(lista)
    comparacoes = 0
    trocas = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1
            if str(lista[j][chave]) > str(lista[j + 1][chave]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
    return lista, comparacoes, trocas

# ----------------------------
# STREAMLIT APP
# ----------------------------
st.set_page_config(page_title="Painel Interativo de Dados", layout="wide")
st.title("📊 Painel Interativo de Ordenação e Análise de Dados")

arquivo = st.file_uploader("📁 Envie um arquivo CSV", type="csv")

if arquivo:
    try:
        df = pd.read_csv(arquivo)
        st.success("✅ Arquivo carregado com sucesso!")

        
        # ============================
        # FILTROS DE BIOMA E MUNICÍPIO
        # ============================

        if "bioma" in df.columns:
            biomas = sorted(df["bioma"].dropna().unique().tolist())
            biomas_selecionados = st.multiselect("🌱 Filtrar por Bioma:", biomas, default=biomas)
            df = df[df["bioma"].isin(biomas_selecionados)]

        if "municipio" in df.columns:
            municipios = sorted(df["municipio"].dropna().unique().tolist())
            municipios_selecionados = st.multiselect("🏙️ Filtrar por Município:", municipios, default=municipios[:10])
            df = df[df["municipio"].isin(municipios_selecionados)]

        # ============================
        # SELEÇÃO DE CRITÉRIO DE ORDENAÇÃO
        # ============================
        colunas_disponiveis = ["data_pas", "bioma", "municipio" ]
        colunas_validas = [c for c in colunas_disponiveis if c in df.columns]

        criterio = st.selectbox("📌 Escolha o critério de ordenação:", colunas_validas)

        if st.button("🔄 Ordenar"):
            dados = df.to_dict(orient="records")
            dados_ordenados, comparacoes, trocas = bubble_sort(dados, criterio)
            df_ordenado = pd.DataFrame(dados_ordenados)

            st.subheader("📋 Todos os dados ordenados")
            st.dataframe(df_ordenado)

            st.markdown(f"🔍 Comparações: `{comparacoes}`  |  🔁 Trocas: `{trocas}`")


            # FUNCIONALIDADE 1: EXPORTAÇÃO
            st.subheader("💾 Baixar Dados Ordenados")
            csv = df_ordenado.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Baixar CSV", data=csv, file_name="dados_ordenados.csv", mime='text/csv')

           
    except Exception as e:
        st.error(f"❌ Erro ao processar o arquivo: {e}")

else:
    st.info("⬆️ Por favor, envie um arquivo CSV para começar.")
