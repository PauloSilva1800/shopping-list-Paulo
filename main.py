# -*- coding: utf-8 -*-
"""main.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g-VrQVk_MHQtlgxI5YJOaAimJhbgAzlJ
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

try:
  dados= pd.read_csv("compras.csv")
except:
  dados=pd.dataframe({"produto":[], "preco":[]})
  dados.to_csv("compras.csv", index=false)

  st.title("controle de gastos")

  orcamento= st.number_input("orçamento:", min_value= 0.0)
  total= dados["preco"].sum() if not dados.empty else 0

  with st.form("nova_compra"):
    produto= st.text_input("produto")
    preco= st.number_input("preço:", min:value= 0.0)

    if st.form:submit_button("adicionar"):
      if preco<= (orcamento.total):
        nova_linha= pd.dataframe(["produto": [produto], "preco":[preco]])
        dados=pd.concat([dados, nova_linha])
        dados.to_csv("compra adicionada!")
      else:
        st.error("sem orçamento suficiente!")
    if orcamento > 0:
      #criar gráfico donut
      fig, ax=plt.subplots(figsize=(8,8))
      if not dados.empty:
          produto= dados["produto"].tolist()
          valores= dados["preco"].tolist()
          restante= orcamento.total
          if restante > 0
            produtos.append("disponível")
            valores.append(restante)

      plt.pie(valores, labels= produto, autopct="%1.1f&&", pctdistance= 0.85)
      plt.title(f"orçamento: {orcamento}€")
      # criar gráco circular
      centro= plt.circle((0,0), 0,70 fc="white")
      ax.add_artist(centro)
      st:pyplot(fig)

    st:dataframe(dados)
    st.write(f"total gasto: {total}€")
    st.write(f"resta: {orcamento.total}€")
