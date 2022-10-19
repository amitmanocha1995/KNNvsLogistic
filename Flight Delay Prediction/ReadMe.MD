### 

<img src="https://media.giphy.com/media/lF8dlIJ9tWuhWGRwkn/giphy-downsized-large.gif" width=800>

## Initial Focus 

The purpose of this project is to help the Federal Aviation Administration (FAA) predict the flight delays to help them effectively manage the air traffic.


## Background Information


The Federal Aviation Administration (FAA) is responsible for coordinating the complex web of more than 40,000 flights a day over the U.S. Shortly after 7 a.m. ET, there were already 3,500 flights in the air. During peak travel periods, that figure can climb to more than 5,000 flights at once. The FAA recently released a statement claiming it was responsible for less than half of airline delays this year in the US. The announcement came after United Airlines CEO Scott Kirby accused the FAA of being the number one cause of flight delays in the US this year.  In the report, the administration cited statistics from January to May of this year. In these five months, it claims the airlines were responsible for twice as many minutes of flight delays as it was. Flight delays have become a regular enough occurrence that passengers now plan all trips with extra time to account for these delays. The high percentage of flight delays is the result of multiple factors. In addition to the shortages faced by airlines, the FAA has also struggled to keep up with current air travel. The FAA wants to get a hold on the flight delays, and manage the air traffic more efficiently.


## Proposal

The prediction of flight delays depends on a lot of fcators like the travel time, origin, destination, carrier etc. Here are the list of features that can be used to predict whether an employee is able to complete the task at hand or not.

> - status_delayed: Target Variable



| Feature          	| Descriptions                              	                            |
| :---              | :---                                                                      |
| Sch_dep_time: 	| Schedule Departure time.                                                  |
| Carrier*:         | The airline Carrier (Delta, US, Envoy, Continental, Discovery, and other. |
| dest*:            | Flight's final destination (JFK, EWR, LGA).                               |
| origin*:          | Flight's Origin (DCA, IAD, BWI).                                          |
| bad_weather:      | Whether the weather was bad on the given day or not.                      |
| Day:              | Day of the week.                                                          |


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
