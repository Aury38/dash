import streamlit as st
import pandas as pd
import plotly.express as px

#CONFIGURANDO O LAYOULT DA PAGINA
st.set_page_config (layout='wide')

df = pd.read_excel(
    io='carteira.xlsx'
)
