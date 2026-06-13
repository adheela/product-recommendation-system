import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Load pickle files
# -----------------------------
df = pickle.load(open("df.pkl", "rb"))
similarity_matrix = pickle.load(open("similarity.pkl", "rb"))

# -----------------------------
# Fast lookup map
# -----------------------------
name_to_index = pd.Series(df.index, index=df["product_name"]).to_dict()

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(product_name, top_n=5):

    if product_name not in name_to_index:
        return pd.DataFrame()

    idx = name_to_index[product_name]

    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    recommended_idx = [i[0] for i in sim_scores]

    return df.loc[recommended_idx, ["product_name", "category", "rating"]]


# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="Product Recommendation System", layout="wide")

st.title("🛒 Amazon Product Recommendation System")
st.write("Select a product and get similar recommendations based on content similarity.")

# Dropdown
product_list = df["product_name"].tolist()
selected_product = st.selectbox("Choose a Product", product_list)

# Button
if st.button("Get Recommendations"):

    results = recommend(selected_product, top_n=5)

    if results.empty:
        st.warning("No recommendations found")
    else:
        st.write("### Top Recommendations")
        st.dataframe(results, use_container_width=True)