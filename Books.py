import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer_reviews.csv")
df_top_100_books = pd.read_csv("datasets/top_100_books.csv")

price_max = df_top_100_books["book price"].max()
price_min = df_top_100_books["book price"].min()

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
df_books = df_top_100_books[df_top_100_books["book price"] <= max_price]

fig_1 = px.bar(df_books["year of publication"].value_counts())
fig_2 = px.histogram(df_books["book price"])
fig_3 = px.histogram(df_books["rating"])
fig_4 = px.bar(df_books["genre"].value_counts())

st.dataframe(df_books.set_index(df_books.columns[0]))

col1, col2 = st.columns(2)
col1.plotly_chart(fig_1)
col2.plotly_chart(fig_2)

col3, col4 = st.columns(2)
col3.plotly_chart(fig_3)
col4.plotly_chart(fig_4)