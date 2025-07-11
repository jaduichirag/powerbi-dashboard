import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/superstore.csv")

st.title("📊 Sales Performance Dashboard")

# Show Data
if st.checkbox("Show Raw Data"):
    st.write(data.head())

# Summary Stats
st.write("## Summary")
st.write(data.describe())

# Plot
st.write("## Sales by Category")
fig, ax = plt.subplots()
sns.barplot(x='Category', y='Sales', data=data, ax=ax)
st.pyplot(fig)