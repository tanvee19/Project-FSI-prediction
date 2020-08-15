import pickle
import numpy as np

with open('model_pickle','rb') as f: 
    classifier = pickle.load(f)

# predicting a value and final value of this case is 2
l=[2.0 , 1.1, 3.6, 2.2, 1.5, 1.6, 0.8, 1.0 , 1.1, 1.5, 2.8, 1.3]
l=np.array(l)
l=l.reshape(1,-1)
pred_1=classifier.predict(l)
print("Prediction is : ",pred_1[0])