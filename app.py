import streamlit as st
import pandas as pd

st.title("Sales Data Dashboard")

data = pd.read_csv("data.csv")

st.subheader("Dataset")
st.write(data)

st.subheader("Sales Chart")
st.bar_chart(data["Sales"])

region = st.selectbox("Select Region", data["Region"].unique())
filtered = data[data["Region"] == region]

st.subheader("Filtered Data")
st.write(filtered)
