                                                                       # %%writefile is used to write the code in this given block to a file called app.py, which will
                                                                       # be created in the same directory. 
import pickle                                                          # Importing the Pickle Library here to execute the app.py file without fail.
import streamlit as st                                                 # Importing the Streamlit library. Streamlit lets you turn data scripts into shareable web apps.
import extra_streamlit_components as stx
import time

pickle_in = open('classifier_workload', 'rb')                                   # Opening Classifier in read-byte mode. 
model_logit = pickle.load(pickle_in)                                   # Pickle load is used to load pickled data from a file-like object.
model_knn = pickle.load(pickle_in)                                     # HEre, pickle is loading both KNN and Logistic regression models.
features = pickle.load(pickle_in)
st.set_page_config(layout="centered")

IMAGE_URL = "https://i.ibb.co/YkKNYSx/asasa.png" 
st.image(IMAGE_URL, width=700)
# <a href="https://ibb.co/JsSfV74"><img src= alt="ese" border="0"></a>
# st.write('Worload Prediction Model')

@st.cache()                                                            # Marking the function with cache decorator (st.cache()) will allow streamlit to keep all the 
                                                                       # states of a function in the memory. Hence, on every refresh the function definition is not executed.
    
def prediction(emp_exp_logit,training_level4,training_level6,training_level8,chosen_id):
    if chosen_id == '1':                                               # Based on the user's preference we are running the model (KNN or Logistic)
        classifier = model_knn
        model = 'KNN'
    else: 
        classifier = model_logit
        model = 'Logistic Regression'
        
        
    prediction = classifier.predict(                                   # method predict() that will essentially use the learned parameters by fit() in order to
                                                                       # perform predictions for each test instance.
        [[emp_exp_logit,training_level4,training_level6,training_level8]])
  
    return (prediction,model)


def main():                                                           # This is the main function in which we define our webpage

    training_level4,training_level6,training_level8=0,0,0             # Using a slide bar to input the employee work experience
    emp_exp_logit = st.slider("Employee Experiences",
                                  min_value=0.0,
                                  max_value=14.00,
                                  value=0.0,
                                  step=0.10,
                                 )

    training_level = st.selectbox('Please select the level of training the employee had',
                              ('Level 4',
                               'Level 6',                            # Creating a drop down to handle the categorical variables.
                               'Level 8'
                              )
                                 )
               
    if training_level=='Level 4':                                    # Based on the used's preference populating the training_level4, training_level6, training_level8 columns in dataset.
                                  training_level4 =1
    elif training_level=='Level 6':
                                  training_level6 =1
    elif training_level=='Level 8':
                                  training_level8 =1
            
    emp_exp_logit = (emp_exp_logit-features[0][0])/features[1][0]



            
    chosen_id = stx.tab_bar(data=[                                   # Allowing user to choose between the models.
    stx.TabBarItemData(id=1, title="KNN Classifier", description="FPR: 0% | Precision: 100% | Accuracy: 90%"),
    stx.TabBarItemData(id=2, title="Logistic Regression", description="FPR: 0% | Precision: 100% | Accuracy: 90%"),
    ],default=1)
    st.info('Recommendation based on the AUC-ROC Curve: Logistic Regression', icon="ℹ️")

  
    result = ""
                                  
    if st.button("Predict"):                                          # When 'Predict' is clicked(using st.button), make the prediction and store it in result.
        results = prediction(emp_exp_logit,training_level4,training_level6,training_level8,chosen_id)
        with st.spinner('Running the '+results[1]+' model'):
            time.sleep(1)
            if results[0] == 0:
                st.error('Task will not be completed!', icon="🚨")
            else:
                st.success('Task will be completed!', icon="✅")
#                 st.balloons()
            

            
if __name__=='__main__':                                              # The value of __name__ attribute is set to “__main__” when module is run as main program. 
    main()
    
