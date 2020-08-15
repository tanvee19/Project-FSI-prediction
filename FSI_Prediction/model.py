# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset and intialising the columns
data = pd.read_csv('yearwisedata.csv', delimiter = ',')

# initialising the features 
features = data.iloc[:, 4:].values

# initialising the labels datset
labels_data = pd.DataFrame(data.iloc[:,3].values)
labels_data[1]=0
for i in range(len(labels_data)):
    num=labels_data[0][i]
    if num >=0 and num<20:
        labels_data[1][i]=1
    elif num >=20 and num<40:
        labels_data[1][i]=2
    elif num >=40 and num<60:
        labels_data[1][i]=3
    elif num >=60 and num<80:
        labels_data[1][i]=4
    elif num >=80 and num<100:
        labels_data[1][i]=5
    elif num >=100 and num<120:
        labels_data[1][i]=6
    else:
        labels_data[1][i]=7

# initialising the labels      
labels=labels_data.iloc[:,1].values
              
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.10, random_state = 0)



#navive bayes MultinomialNB GaussianNB
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
gnb = GaussianNB()
gnb.fit(features_train, labels_train)
score_gnb = gnb.score(features_test,labels_test)
print("Score of GaussianNB is ",round(score_gnb,2))

#navive bayes MultinomialNB
mnb = MultinomialNB()
mnb.fit(features_train, labels_train)
score_mnb = mnb.score(features_test,labels_test)
print("Score of MultinomialNB is ",round(score_mnb,2))

# navive bayes BernoulliNB
bnb = BernoulliNB()
bnb.fit(features_train, labels_train)
score_bnb = bnb.score(features_test,labels_test)
print("Score of BernoulliNB is ",round(score_bnb,2))

# Fitting Knn to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)
score_kns = classifier.score(features_test,labels_test)
print("Score of KNeighborsClassifier is ",round(score_kns,2))

# kernels: linear, poly and rbf
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)
score_svc_rbf = classifier.score(features_test,labels_test)
print("Score of Rbf SVC is ",round(score_svc_rbf,2))

# kernels: linear, poly and rbf
classifier = SVC(kernel = 'poly', random_state = 0)
classifier.fit(features_train, labels_train)
score_svc_poly = classifier.score(features_test,labels_test)
print("Score of Poly SVC is ",round(score_svc_poly,2))

# kernels: linear, poly and rbf
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(features_train, labels_train)
score_svc_linear = classifier.score(features_test,labels_test)
print("Score of Linear SVC is ",round(score_svc_linear,2))

# Random Forest Score
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  
score_randomforest = classifier.score(features_test,labels_test)
print("Score of Random Forest is ",round(score_randomforest,2))

#Training and making predictions using DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)
score_decisiontree = classifier.score(features_test,labels_test)
print("Score of Decision Tree is ",round(score_decisiontree,2))

# training ogistic regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)
score_lr = classifier.score(features_test,labels_test)
print("Score of Logistic regression is ",round(score_lr,2))
        