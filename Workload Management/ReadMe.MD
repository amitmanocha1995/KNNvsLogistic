
### 


<img src="https://media.giphy.com/media/2ae1SlEEdw1Qvc3KCA/giphy.gif" width=800>



## Initial Focus 

The purpose of this project is to create a classification model for the Human Resource department to help them make better decisions about the team assignments.

## Background Information

Work allocation is the process of effectively organizing resources and labor to meet the company's output goals of a task or project. The allocation is based on how the business will benefit from appropriately assigning resources and roles. Management can start by assessing the project's requirements in terms of the required skillset. This would be based on the employee's abilities, qualifications and experience, with each task being allocated to the best person for the role. The assigned staff member should be able to deliver on the requirements. The employees have gone through several tranings in the past, which is inluded in the dataset. On the basis of which employee can complete a particular task, they will be alocated to several teams to effectively manage the workload.


## Proposal

The work allocation process depends on a lot of factors like the experience of the employee or the level of training they have had during their duration. Here are the list of features that can be used to predict whether an employee is able to complete the task at hand or not.

> - task_completed: Target Variable



| Feature          	| Descriptions                              	|
| :---              | :---                                          |
| Employee Exp: 	| Number of years of experience an employee has.|
| Training Level 4: | Whether an employee has had Level 4 Training. |
| Training Level 6: | Whether an employee has had Level 6 Training. |
| Training Level 8: | Whether an employee has had Level 8 Training. |
| Task Completed:   | Whether an employee has completed the task.   |


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
