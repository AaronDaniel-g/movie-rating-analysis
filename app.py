import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("🎬 Movie Rating Analysis")

# Load dataset
df = pd.read_csv("movies.csv")

# Show dataset
st.subheader("📄 Movie Dataset")
st.write(df)

# Top Rated Movies
st.subheader("⭐ Top Rated Movies")
top_movies = df.sort_values(by="Rating", ascending=False)
st.write(top_movies)

# Average Rating
st.subheader("📊 Average Movie Rating")
average_rating = df["Rating"].mean()
st.success(f"Average Movie Rating: {average_rating:.2f}")

# Rating Distribution Graph
st.subheader("📈 Rating Distribution")
fig, ax = plt.subplots()
sns.histplot(df["Rating"], bins=5, kde=True, ax=ax)
st.pyplot(fig)

# Genre Count
st.subheader("🎭 Movies by Genre")
genre_count = df["Genre"].value_counts()
fig2, ax2 = plt.subplots()
genre_count.plot(kind="bar", ax=ax2)
st.pyplot(fig2)