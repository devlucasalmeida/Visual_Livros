import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer_reviews.csv")
df_top_100_books = pd.read_csv("datasets/top_100_books.csv")

books = df_top_100_books["book title"].unique()

book = st.sidebar.selectbox("books", books)

df_book = df_top_100_books[df_top_100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = df_book["book price"].iloc[0]
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
col1.metric("Price", f"${book_price}")
col2.metric("Rating", book_rating)
col3.metric("Year of publication", book_year)

st.divider()

for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.markdown(f'<div style="text-align: justify;">{row[5]}</div>', unsafe_allow_html=True)