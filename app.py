import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("amazon.csv")
df = df.dropna().reset_index(drop=True)

# -----------------------------
# Text feature
# -----------------------------
df["text"] = (
    df["product_name"].astype(str) + " " +
    df["category"].astype(str) + " " +
    df["about_product"].astype(str)
)

# -----------------------------
# TF-IDF + Similarity
# -----------------------------
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["text"])
similarity_matrix = cosine_similarity(tfidf_matrix)

# -----------------------------
# Recommendation Function (your logic)
# -----------------------------
def recommend(product_name, top_n=5):

    matches = df[df["product_name"].str.contains(product_name, case=False, na=False)].index.tolist()

    if not matches:
        return pd.DataFrame()

    idx = matches[0]

    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    recommended_idx = [i[0] for i in sim_scores]

    return df.loc[recommended_idx, ["product_name", "category", "rating"]]


# -----------------------------
# STREAMLIT UI
# -----------------------------
st.title("🛒 Amazon Product Recommendation System")

st.write("Select a product and get similar recommendations")

# Dropdown
product_list = df["product_name"].tolist()
selected_product = st.selectbox("Choose Product", product_list)

# Button
if st.button("Get Recommendations"):

    results = recommend(selected_product, top_n=5)

    if results.empty:
        st.warning("No recommendations found")
    else:
        st.write("### Top Recommendations")
        st.dataframe(results)