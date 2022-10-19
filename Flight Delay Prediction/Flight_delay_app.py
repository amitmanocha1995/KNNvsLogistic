                                                                       # %%writefile is used to write the code in this given block to a file called app.py, which will
                                                                       # be created in the same directory. 
import pickle                                                          # Importing the Pickle Library here to execute the app.py file without fail.
import streamlit as st                                                 # Importing the Streamlit library. Streamlit lets you turn data scripts into shareable web apps.
import extra_streamlit_components as stx
import time

pickle_in = open('classifier_flight', 'rb')                                   # Opening Classifier in read-byte mode. 
model_logit = pickle.load(pickle_in)                                   # Pickle load is used to load pickled data from a file-like object.
model_knn = pickle.load(pickle_in)                                     # HEre, pickle is loading both KNN and Logistic regression models.
features = pickle.load(pickle_in)
st.set_page_config(layout="centered")

IMAGE_URL = "https://i.ibb.co/8gfCxvR/flight-img.png"
st.image(IMAGE_URL, width=700)


@st.cache()                                                            # Marking the function with cache decorator (st.cache()) will allow streamlit to keep all the 
                                                                       # states of a function in the memory. Hence, on every refresh the function definition is not executed.
    
def prediction(sch_dep_time, carrier_delta, carrier_us, carrier_envoy, carrier_continental, carrier_discovery, carrier_other, dest_jfk, dest_ewr, dest_lga, distance, origin_dca, origin_iad, origin_bwi, bad_weather, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, chosen_id):
    if chosen_id == '1':                                               # Based on the user's preference we are running the model (KNN or Logistic)
        classifier = model_knn
        model = 'KNN'
    else: 
        classifier = model_logit
        model = 'Logistic Regression'
       
    prediction = classifier.predict(                                   # method predict() that will essentially use the learned parameters by fit() in order to
                                                                       # perform predictions for each test instance.
        [[sch_dep_time, carrier_delta, carrier_us, carrier_envoy, carrier_continental, carrier_discovery, carrier_other, dest_jfk, dest_ewr, dest_lga, distance, origin_dca, origin_iad, origin_bwi, bad_weather, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]])
  
    return (prediction,model)


def main():                                                           # This is the main function in which we define our webpage

    carrier_delta,carrier_us,carrier_envoy,carrier_continental,carrier_discovery,carrier_other=0,0,0,0,0,0             # Using a slide bar to input the employee work experience
    sch_dep_time = st.slider("Scheduled Departure time",
                                  min_value=0.0,
                                  max_value=22.00,
                                  value=0.0,
                                  step=0.10,
                                 )

    carriers = st.selectbox('Please select the carrier',
                              ('Delta',
                               'US',                            # Creating a drop down to handle the categorical variables.
                               'Envoy',
                               'Continental',
                               'Discovery',
                               'Others'
                              )
                                 )
               
    if carriers=='Delta':                                    # Based on the used's preference populating the training_level4, training_level6, training_level8 columns in dataset.
                                  carrier_delta =1
    elif carriers=='US':
                                  carrier_us =1
    elif carriers=='Envoy':
                                  carrier_envoy =1
    elif carriers=="Continental":
                                  carrier_continental=1
    elif carriers=="Discovery":
                                  carrier_discovery=1
    elif carriers=="Others":
                                  carrier_other=1
            
    dest_jfk, dest_ewr, dest_lga=0,0,0
            
    destination = st.selectbox('Please select the Destination',
                              ('JFK',
                               'EWR',                            # Creating a drop down to handle the categorical variables.
                               'LGA'
                              )
                                 )  
    if destination == "JFK":
        dest_jfk = 1
    elif destination == "EWR":
        dest_ewr = 1
    elif destination == "LGA":
        dest_lga = 1
        
        
    distance = st.slider("Distance",
                                  min_value=160,
                                  max_value=230,
                                  value=0,
                                  step=1,
                                 )
        
    origin_dca,origin_iad,origin_bwi = 0,0,0  
    origins = st.selectbox('Please select the Origin',
                          (
                          "DCA",
                          "IAD",
                          "BWI"
                          )
                          )
    if origins == "DCA":
        origin_dca =1
    elif origins == "IAD":
        origin_iad = 1
    elif origins == "BWI":
        origin_bwi = 1
    
    bad_weather = 0
    
    weather = st.radio(
    "Weather conditions:",
    ('Good', 'Bad'))

    if weather == 'Good':
        bad_weather = 0
    else:
        bad_weather = 1
    
    weekday = st.selectbox('Please select the Day of the Week',
                          (
                          "Monday",
                          "Tuesday",
                          "Wednesday",
                          "Thursday",
                              "Friday",
                              "Saturday",
                              "Sunday"
                          )
                          )
    Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday = 0,0,0,0,0,0,0 
    
    if weekday == "Monday":
        Monday = 1
    elif weekday == "Tuesday":
        Tuesday = 1
    elif weekday == "Wednesday":
        Wednesday = 1
    elif weekday == "Thursday":
        Thursday = 1
    elif weekday == "Friday":
        Friday = 1
    elif weekday == "Saturday":
        Saturday = 1
    elif weekday == "Sunday":
        Sunday = 1
        
        
    sch_dep_time = (sch_dep_time-features[0][0])/features[1][0]
    distance = (distance-features[0][1])/features[1][1]

    
    chosen_id = stx.tab_bar(data=[                                   # Allowing user to choose between the models.
    stx.TabBarItemData(id=1, title="KNN Classifier", description="F-1 Score: 40% | Accuracy: 53%"),
    stx.TabBarItemData(id=2, title="Logistic Regression", description="F-1 Score: 41% | Accuracy: 58%"),
    ],default=1)
    st.info('Recommendation based on the AUC-ROC Curve: Logistic Regression', icon="ℹ️")

  
    result = ""
                                  
    if st.button("Predict"):                                          # When 'Predict' is clicked(using st.button), make the prediction and store it in result.
        results = prediction(sch_dep_time, carrier_delta, carrier_us, carrier_envoy, carrier_continental, carrier_discovery, carrier_other, dest_jfk, dest_ewr, dest_lga, distance, origin_dca, origin_iad, origin_bwi, bad_weather, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, chosen_id)
        with st.spinner('Running the '+results[1]+' model'):
            time.sleep(1)
            if results[0] == 0:
                st.error('Flight will be delayed!', icon="🚨")
            else:
                st.success('Flight will be on-time!', icon="✅")
#                 st.balloons()
            

            
if __name__=='__main__':                                              # The value of __name__ attribute is set to “__main__” when module is run as main program. 
    main()
    
