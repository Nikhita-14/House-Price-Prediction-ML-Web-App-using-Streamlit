import streamlit as st
import pandas
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data=pandas.read_csv("house_prices.csv")
X=data[["Area_sqft","Bedrooms","Bathrooms"]]
y=data["Price"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=LinearRegression()
model.fit(X_train,y_train)

joblib.dump(model,"house_price_model.pkl")
print("Model done and saved in pkl file")

model=joblib.load("C:\\Users\\study\\Desktop\\House Price Prediction Web App\\house_price_model.pkl")
st.title("House Prices")
area=st.number_input("Enter the area (sqft)", min_value=500, max_value=5000)
bedrooms=st.number_input("Enter the number of bedrooms", min_value=1, max_value=5)
bathrooms=st.number_input("Enter the number of bathrooms", min_value=1, max_value=5)

if st.button("Predict Price"):
    prediction=model.predict([[area, bedrooms, bathrooms]])
    st.success(f"Estimated Price: {prediction[0]:.2f}")

avg_price_by_bedroom=data.groupby("Bedrooms")["Price"].mean()
st.subheader("Average Price by Number of Bedrooms")
st.bar_chart(avg_price_by_bedroom)