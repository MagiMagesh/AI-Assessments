# AI-Assessments

# About Dataset:

1. Dataset has 154 Features
2. In which many labels are highly correlated with each other
3. Some Features shown the S.D of 0
4. 20-30 Features had High varience and outliers.
5. Brought Many Features to Standard Normal Distributions.
6. Since There are many features have to do ** Clustering of the Features ** and find the best fit model for individual Clustering.

# Work Progress in Dataset:

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
