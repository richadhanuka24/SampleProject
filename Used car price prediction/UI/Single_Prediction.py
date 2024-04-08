
import streamlit as st
import pickle
import numpy as np


st.title("Welcome to my used cars portal")
st.header("Please enter your car details here")

kms=st.number_input("Enter Kms",0,10000,100)
car_age=st.number_input("Enter car age",0,50)
original_price=st.number_input("Enter the original price",100000,5000000)
fuel=st.radio("Select fuel type",('Petrol','Disel','CNG'))
transmission=st.selectbox("Select transmission type",['Manual','Automatic'])

#create a button to predict output
predict_clicked=st.button("Get the car price")

if predict_clicked==True:
    model=pickle.load(open("MLModel-car\Model\car_model.pkl", 'rb'))
    if fuel=='Petrol':
        fuel=list([0,1])
    elif fuel=='Disel':
        fuel=list([1,0])
    else:
        fuel=list([0,0])
    
    if transmission=='Manual':
        transmission=1
    else:
        transmission=0
    
    #calling the model

    #load the test data into numpy array
    data=[np.array([kms,car_age,original_price,fuel[0],fuel[1],transmission])]

    #call the model to predict the price
    result=model.predict(data)
    

    #display the predicted price on the webpage
    st.success("The predicted price for your Car is"+ str(result))



