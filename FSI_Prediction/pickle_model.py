# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# kernels: linear, poly and rbf
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(features_train, labels_train)
score_svc_linear = classifier.score(features_test,labels_test)
print("Score of Linear SVC is ",round(score_svc_linear,2))

# prediction of Features to be tested
labels_pred=classifier.predict(features_test)

# finding confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

# predicting a value and final value of this case is 2
l=[2.0 , 1.1, 3.6, 2.2, 1.5, 1.6, 0.8, 1.0 , 1.1, 1.5, 2.8, 1.3]
l=np.array(l)
l=l.reshape(1,-1)
pred_1=classifier.predict(l)
print("Prediction is : ",pred_1[0])



import pickle
with open('model_pickle','wb') as f:
    pickle.dump(classifier,f)
