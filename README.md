## Created a Machine learning Project That allows you to Pridict creadit code score
Processes used to create the project
- Data Cleaning and Data Pre-Processing is done to clean the data so that its easy to work with for futher process
- The data has 28 diffrenet columns
- All Duplicates and data is cleaned using pandas

Data Visulization
- Data visulization is done to look for inghts in the data so that correation can be found which will be usefull in creating the ml model
  
  ![image](https://github.com/user-attachments/assets/fda6d4a6-00f3-40dd-8fe3-85234515bf0e)

Creating a ML model
- Modeling
  ``` 
  columns = [  'Age'  ,  'interest_rate'    , 'Delay_from_due_date'   , 'Num_of_Delayed_Payment' , 'num_bank_accounts'  , 'num_credit_cards' , 'Outstanding_Debt'  , 'Annual_Income' ]

  X_train = np.array(X_train[columns])
  X_test = np.array(X_test[columns]) ```
- Using Loggistics Reggration
  - Encoding Occupation to Numerical Values for Easy use Also encoding payment_of_min_amount
  - 
  - 
