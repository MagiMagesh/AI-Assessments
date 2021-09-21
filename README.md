# AI-Assessments
1. Dataset of Music labels.
2. Normalising, Feature Selection, Feature Modeling, Model prediction, testing
3. Feature Selection,
	1. Threshold
	2. ExtraTreesClassifier
	3. Mutual info dropping
	4. PCA

	From this after testing all the possibilities PCA give the best accuracy
4. Model Selection
	1. Logistic Regression
	2. RandomForestClassifier
	3. Decision Trees
	4. XG Boost
	5. KNN
	6. SVC
	7. Ensembling of KNN, SVC, RFC
	
	From these Models RFC and XG Boost Gives the same level of accuracy. So choosed the XG Boost.
  
  
Created a Flask App to works in Postman:
  
![POST](https://user-images.githubusercontent.com/86392043/134184740-b08897d8-57c8-4adb-a2c2-b70dbdce29a2.PNG)

Created a Flask App to works in Swagger:

![Swagger](https://user-images.githubusercontent.com/86392043/134184899-f89a10eb-1a9a-4cb7-830c-dffdc2892c15.PNG)
