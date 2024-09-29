import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv('ex_car_rental_data.csv')

df = load_data()

# App title
st.title('Car Rental Recommendation System')

# Dataset display option
if st.checkbox('Show Available Cars Dataset'):
    st.dataframe(df)

# User inputs for recommendation
st.sidebar.header('User Preferences')
category = st.sidebar.selectbox("Select Car Category", df['Category'].unique())
fuel_type = st.sidebar.selectbox("Select Fuel Type", df['Fuel Type'].unique())
num_seats = st.sidebar.slider("Number of Seats", min_value=int(df['Number of Seats'].min()), max_value=int(df['Number of Seats'].max()), step=1)
air_conditioning = st.sidebar.selectbox("Air Conditioning", df['Air Conditioning'].unique())
budget = st.sidebar.number_input("Enter your budget (INR)", min_value=0)

# Filter dataset based on user inputs
filtered_df = df[
    (df['Category'] == category) &
    (df['Fuel Type'] == fuel_type) &
    (df['Number of Seats'] == num_seats) &
    (df['Air Conditioning'] == air_conditioning) &
    (df['Price Per Day (INR)'] <= budget)
]

# Display results
st.subheader('Recommended Cars')
if not filtered_df.empty:
    st.write(f"Cars matching your preferences:")
    st.dataframe(filtered_df)
else:
    st.write("No cars match your preferences.")
