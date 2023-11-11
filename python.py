import numpy as np
import pickle
import streamlit as st #create account in Streamlit
#map the data
#location,status,property type and facing
location_mapping = {
    "Kesarapalli":10,
    "Auto Nagar":12,
    "Poranki": 8,
    "Kankipadu": 5,
    "Benz Circle": 0,
    "Gannavaram": 2,
    "Rajarajeswari Peta": 9,
    "Gunadala": 4,
    "Gollapudi": 3,
    "Enikepadu": 1,
    "Vidhyadharpuram": 11,
    "Penamaluru": 7,
    "Payakapuram": 6}
#in smilar way we do for status,facing and property type
status_mapping = {'Ready to move':1,
                  'New':0,'Resale':2,'Under Construction':3}
direction_mapping={"None":1,
            "East":0,
            "West":8,
            "NorthEast":3,
            "NorthWest":4,
            "North":2,
            "South":5,
            "SouthEast":6,
            "SouthWest":7}
property_type_mapping={"Apartment":0,
            "Independent Floor":1,
            "Independent House":2,
            "Residential Plot":3,
            "Studio Apartment":4,
            "Villa":5}
#reading pickle file 
with open("House.pkl",'rb') as f:
    model=pickle.load(f)
#create a function to accept inputs and create an array
def predict(bed,bath,loc,size,status,facing,Type):
  """Function to accept data"""
  selected_location=location_mapping[loc]
  selected_status=status_mapping[status]
  selected_direction=direction_mapping[facing]
  selected_property=property_type_mapping[Type]
  input_data=np.array([[bed,bath,selected_location,size,selected_status,selected_direction,selected_property]])
  return model.predict(input_data)[0]

if __name__=="__main__":
    st.header("House Price Prediction")
    st.title("Just started")
  
  
    







