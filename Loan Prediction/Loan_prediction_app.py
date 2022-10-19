                                                                       # %%writefile is used to write the code in this given block to a file called app.py, which will
                                                                       # be created in the same directory. 
import pickle                                                          # Importing the Pickle Library here to execute the app.py file without fail.
import streamlit as st                                                 # Importing the Streamlit library. Streamlit lets you turn data scripts into shareable web apps.
import extra_streamlit_components as stx
import time
import numpy as np

pickle_in = open('classifier_loan', 'rb')                                   # Opening Classifier in read-byte mode. 
model_logit = pickle.load(pickle_in)                                   # Pickle load is used to load pickled data from a file-like object.
model_knn = pickle.load(pickle_in)                                     # HEre, pickle is loading both KNN and Logistic regression models.
features = pickle.load(pickle_in)
st.set_page_config(layout="centered")

IMAGE_URL = "https://i.ibb.co/8gfCxvR/flight-img.png"
st.image(IMAGE_URL, width=700)


@st.cache()                                                            # Marking the function with cache decorator (st.cache()) will allow streamlit to keep all the 
                                                                       # states of a function in the memory. Hence, on every refresh the function definition is not executed.
    
def prediction(gender, age, debt, married, bank_customer,emp_industrial, emp_materials, emp_consumer_services,emp_healthcare, emp_financials, emp_utilities, emp_education,ethnicity_white, ethnicity_black, ethnicity_latino,ethnicity_asian, ethnicity_other, years_employed, prior_default,employed, credit_score, drivers_license, citizen_bybirth,citizen_other, citizen_temporary, Income, chosen_id):
    if chosen_id == '1':                                               # Based on the user's preference we are running the model (KNN or Logistic)
        classifier = model_knn
        model = 'KNN'
    else: 
        classifier = model_logit
        model = 'Logistic Regression'
       
    prediction = classifier.predict(                                   # method predict() that will essentially use the learned parameters by fit() in order to
                                                                       # perform predictions for each test instance.
        [[gender, age, debt, married, bank_customer,emp_industrial, emp_materials, emp_consumer_services,emp_healthcare, emp_financials, emp_utilities, emp_education,ethnicity_white, ethnicity_black, ethnicity_latino,ethnicity_asian, ethnicity_other, years_employed, prior_default,employed, credit_score, drivers_license, citizen_bybirth,citizen_other, citizen_temporary, Income]])
  
    return (prediction,model)


def main():                                                           # This is the main function in which we define our webpage's components

    gender = 0
    
    sex = st.radio("Gender ",('Male', 'Female'))

    if sex == 'Male':
        gender = 0
    else:
        gender = 1

        
    age = 0    
    age = st.slider("Age ",
                                  min_value=13.0,
                                  max_value=81.00,
                                  value=0.0,
                                  step=0.10,
                                 )


    debt = st.slider("Debt ",
                                  min_value=0.0,
                                  max_value=30.00,
                                  value=0.0,
                                  step=0.10,
                                 )
    
    married = 0
    
    m = st.radio("Marital Status ",('Married', 'Single'))

    if m == 'Male':
        married = 0
    else:
        married = 1

        
    bank_customer = 0
    
    b = st.radio("Current Customer ",('Yes', 'No'))

    if b == 'Yes':
        bank_customer = 0
    else:
        bank_customer = 1
        
        
    pe = st.selectbox('Previous Employer',
                          (
                          "Industrial",
                          "Materials",
                          "Consumer Services",
                          "Healthcare",
                              "Financials",
                              "Utilities",
                              "Education"
                          )
                          )
    emp_industrial, emp_materials, emp_consumer_services, emp_healthcare, emp_financials, emp_utilities, emp_education = 0,0,0,0,0,0,0 
    
    if pe == "Industrial":
        emp_industrial = 1
    elif pe == "Materials":
        emp_materials = 1
    elif pe == "Consumer Services":
        emp_consumer_services = 1
    elif pe == "Healthcare":
        emp_healthcare = 1
    elif pe == "Financials":
        emp_financials = 1
    elif pe == "Utilities":
        emp_utilities = 1
    elif pe == "Education":
        emp_education = 1
        
    
    
    eth = st.selectbox('Ethinicity',
                          (
                          "White",
                          "Black",
                          "Latino",
                          "Asian",
                              "Others",
                              "Utilities",
                              "Education"
                          )
                          )
    ethnicity_white, ethnicity_black, ethnicity_latino, ethnicity_asian, ethnicity_other = 0,0,0,0,0 
    
    if eth == "Industrial":
        ethnicity_white = 1
    elif eth == "Materials":
        ethnicity_black = 1
    elif eth == "Consumer Services":
        ethnicity_latino = 1
    elif eth == "Healthcare":
        ethnicity_asian = 1
    elif eth == "Financials":
        ethnicity_other = 1

        
    years_employed = st.slider("Years of Employment ",
                                  min_value=0.0,
                                  max_value=5.00,
                                  value=0.0,
                                  step=0.10,
                                 )   
        
        
        
    prior_default = 0
    
    pd = st.radio("Prior Default ",('Yes', 'No'))

    if pd == 'Yes':
        prior_default = 1
    else:
        prior_default = 0
        
        
    employed = 0
    
    emp = st.radio("Currently Employed ",('Yes', 'No'))

    if emp == 'Yes':
        employed = 1
    else:
        employed = 0
        
    credit_score = st.slider("Credit Score",
                                  min_value=0.0,
                                  max_value=7.00,
                                  value=0.0,
                                  step=0.05,
                                 )  
        
        
    drivers_license = 0
    
    dl = st.radio("Drivers License ",('Yes', 'No'))

    if dl == 'Yes':
        drivers_license = 1
    else:
        drivers_license = 0
        
        
        
    ctz = st.selectbox('Citizenship',
                          (
                          "By Birth",
                          "Other",
                          "Temporary"
                          )
                          )
    citizen_bybirth, citizen_other, citizen_temporary = 0,0,0
    
    if ctz == "By Birth":
        citizen_bybirth = 1
    elif ctz == "Other":
        citizen_other = 1
    elif ctz == "Temporary":
        citizen_temporary = 1   
        
    Income = st.slider("Income",
                                  min_value=0.0,
                                  max_value=7.00,
                                  value=0.0,
                                  step=0.05,
                                 )  
        
   

    Income = np.log2(Income+1).round(2)   # Taking log as we did before training the model
    years_employed = (years_employed-features[0][0])/features[1][0] # Scaling the model as we did before training the model
    credit_score = (credit_score-features[0][1])/features[1][1]
    age = (age-features[0][2])/features[1][2]
    debt = (debt-features[0][3])/features[1][3]
    

    chosen_id = stx.tab_bar(data=[                                   # Allowing user to choose between the models.
    stx.TabBarItemData(id=1, title="KNN Classifier", description="Precision: 92% | Accuracy: 79%"),
    stx.TabBarItemData(id=2, title="Logistic Regression", description="Precision: 91% | Accuracy: 87%"),
    ],default=1)
    st.info('Recommendation based on the AUC-ROC Curve: Logistic Regression', icon="ℹ️")

  
    result = ""
                                  
    if st.button("Predict"):                                          # When 'Predict' is clicked(using st.button), make the prediction and store it in result.
        results = prediction(gender, age, debt, married, bank_customer,emp_industrial, emp_materials, emp_consumer_services,emp_healthcare, emp_financials, emp_utilities, emp_education,ethnicity_white, ethnicity_black, ethnicity_latino,ethnicity_asian, ethnicity_other, years_employed, prior_default,employed, credit_score, drivers_license, citizen_bybirth,citizen_other, citizen_temporary, Income, chosen_id)
        with st.spinner('Running the '+results[1]+' model'):
            time.sleep(1)
            if results[0] == 0:
                st.error('Loan Denied!', icon="🚨")
            else:
                st.success('Loan Approved!', icon="✅")
#                 st.balloons()
            

            
if __name__=='__main__':                                              # The value of __name__ attribute is set to “__main__” when module is run as main program. 
    main()
    
