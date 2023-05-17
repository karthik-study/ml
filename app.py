import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

#Step 1: Load the trained model
model=open('rfc.pickle','rb')
clf=pickle.load(model)
model.close()

#Step 2: Get the user input from the front end (UI)
pregs=st.number_input('Pregnancies',0,20,step=1),
glucose=st.slider('Glucose',40, 200, 40),
bp=st.slider('BloodPressure',20,140,20),
skin=st.slider('SkinThickness',7,99,7),
insulin=st.slider('Insulin',14,820,14),
bmi=st.slider('BMI',18,70,18),
dp=st.slider('DiabetesPedigreeFunction',0.05,2.5,0.5),
age=st.slider('Age',21,90,21)
