import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    page_icon="🏥",
    layout="wide"
)

# -----------------------
# Load Files
# -----------------------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
df = pd.read_csv("insurance.csv")

# -----------------------
# Title
# -----------------------
st.title("🏥 Medical Insurance Cost Prediction Dashboard")
st.markdown("Predict insurance costs using Machine Learning")

# -----------------------
# Sidebar Inputs
# -----------------------
st.sidebar.header("Enter Customer Details")

age = st.sidebar.slider("Age", 18, 100, 25)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

bmi = st.sidebar.slider(
    "BMI",
    10.0,
    50.0,
    25.0
)

children = st.sidebar.slider(
    "Children",
    0,
    10,
    0
)

smoker = st.sidebar.selectbox(
    "Smoker",
    ["No", "Yes"]
)

region = st.sidebar.selectbox(
    "Region",
    ["southwest", "southeast", "northwest", "northeast"]
)

# -----------------------
# Prediction
# -----------------------
if st.sidebar.button("Predict Cost"):

    is_female = 1 if gender == "Female" else 0
    smoker_val = 1 if smoker == "Yes" else 0
    region_southeast = 1 if region == "southeast" else 0
    bmi_category_obese = 1 if bmi >= 30 else 0

    scaled = scaler.transform([[age, bmi, children]])

    age_scaled = scaled[0][0]
    bmi_scaled = scaled[0][1]
    children_scaled = scaled[0][2]

    input_data = np.array([[
        age_scaled,
        is_female,
        bmi_scaled,
        children_scaled,
        smoker_val,
        region_southeast,
        bmi_category_obese
    ]])

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    st.success(
        f"Estimated Insurance Cost: ₹ {prediction:,.2f}"
    )

    # Risk Level
    if prediction < 10000:
        st.success("🟢 Risk Level : LOW")
    elif prediction < 20000:
        st.warning("🟡 Risk Level : MEDIUM")
    else:
        st.error("🔴 Risk Level : HIGH")

# -----------------------
# Dashboard Metrics
# -----------------------
st.subheader("📊 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Records",
        len(df)
    )

with col2:
    st.metric(
        "Average BMI",
        round(df["bmi"].mean(), 2)
    )

with col3:
    st.metric(
        "Average Charges",
        f"₹ {round(df['charges'].mean(),0)}"
    )

with col4:
    st.metric(
        "Smokers",
        df[df["smoker"] == "yes"].shape[0]
    )

# -----------------------
# Graph 1
# -----------------------
st.subheader("📈 Age vs Insurance Charges")

fig1 = px.scatter(
    df,
    x="age",
    y="charges",
    color="smoker"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# -----------------------
# Graph 2
# -----------------------
st.subheader("📈 BMI vs Charges")

fig2 = px.scatter(
    df,
    x="bmi",
    y="charges",
    color="smoker"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# -----------------------
# Graph 3
# -----------------------
st.subheader("📈 Smoker vs Non-Smoker")

fig3 = px.box(
    df,
    x="smoker",
    y="charges",
    color="smoker"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# -----------------------
# Graph 4
# -----------------------
st.subheader("📈 Region-wise Average Charges")

region_data = (
    df.groupby("region")["charges"]
    .mean()
    .reset_index()
)

fig4 = px.bar(
    region_data,
    x="region",
    y="charges",
    color="region"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# -----------------------
# Dataset Preview
# -----------------------
st.subheader("📋 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.markdown(
    "Developed by Bhupendra Chouhan | Data Science Project"
)