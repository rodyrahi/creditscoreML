## Created a Machine learning Project That allows you to Pridict creadit card score
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
  X_test = np.array(X_test[columns])
  
- Using Loggistics Reggration
  - Encoding Occupation to Numerical Values for Easy use Also encoding payment_of_min_amount
  - ```
    clf = LogisticRegression()
    clf.fit(X_train, y_train)

  - Using the code above to fit xtrain , ytrain
  - Train accuracy: 53.32
- Using Random Forest
  - To get better result random forest is used
  - `Train accuracy: 95.04
    Model accuracy: 77.64%`
  - This seams to be the best result I can get
- Classification Report
  `
  
                    precision    recall  f1-score   support
      
                 1       0.74      0.71      0.73      2524
                 2       0.79      0.79      0.79      7704
                 3       0.78      0.78      0.78      4264
      
          accuracy                           0.78     14492
         macro avg       0.77      0.76      0.77     14492
      weighted avg       0.78      0.78      0.78     14492
  

  
