### 

<img src="https://i.ibb.co/TM3LtWV/Financial-logo-hand-dollars-logo.png" width=500>


## Initial Focus 

The purpose of this project is to create a loan prediction model for the Underwriting Team of The Regional Bank of America.


## Background Information

Underwriting is the process of evaluating the risk involved with a financial transaction, such as a bank loan. Manual underwriting processes are inconsistent, lack accuracy, and are time-consuming. Automating your loan process can streamline the work that needs to be completed, offering an accurate and consistent data flow for every step of your loan process.

Automated underwriting is a technology-driven underwriting process that provides a computer generated loan decision. The lending industry is broadly migrating to the use of new technology-driven loan underwriting platforms to improve the processing time for all types of loans.

## Proposal

The prediction of loan approvals depends on a lot of factors like the credit score, age of the customer, delinquent history, income etc. Here are the list of features that can be used to predict whether a loan for an individual could be approved or not. 

> - approved: Target Variable



| Feature          	| Descriptions                              	                            |
| :---              | :---                                                                      |
| gender: 	| Gender of the customer.                                                  |
| age:         | Age of the customer. |
| bank_customer:            | Whether the person is a customer at the bank or not.                               |
| Emp_*:          | Which industry does the customer works in (Industrial, Materials, Comsumer_Services, Healthcare etc.  |
| Ethnicity_*:      | Ethnicity of the customer (White, Black, Latino, Asian, other).                 |
| years_employed:         | Number of years the Custromer is working for.                                      |
| credit_score:         | Credit score of the customer.                                      |
| drivers_license:         | Whether the customer has the driver's license or not.                                      |
| Citizen*:         | Is the customer a citizen of the United States.(bybirth, other, teporary)                             |
| Income:         | Income of the customer.                                      |


## Specification

- Python: 3.9.12
- Pandas: 1.4.3
- Seaborn: 0.11.2
- sklearn: 1.1.2.
- Numpy: 1.21.5

This data contains the data of overall 75 employees.  The target variable of interest is task_completed. The data was provided as a part of our CIS: 508 Assignment.


## Table of Contents: <a class="anchor" id="steps"></a>
- [1. Libraries & Custom Functions](#libraries)
- [2. Data Wrangling](#wrangle)
   - [2.1 Data Gathering](#gather)
   - [2.2 Data Assessment](#assess)
   - [2.3 Data Cleaning](#clean)
- [3. Model Building](#model)
    - [3.1 Model 1](#model001)
    - [3.2 Model 2](#model002)
- [4. Model Comparison](#comparison)
- [5. Model Evaluation](#evaluation)
- [6. Conclusion](#conclusion)
- [7. Deployment](#deployment)

