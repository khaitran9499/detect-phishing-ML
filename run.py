#importing libraries
import joblib
import feature_extraction
import numpy as np
#load the pickle file
classifier = joblib.load('random_forest_model.pkl')

#input url
url = input("Enter url:")

#checking and predicting
checkprediction = feature_extraction.generate_data_set(url)
checkprediction = np.array(checkprediction).reshape(1,-1)

try:
   prediction = classifier.predict(checkprediction)
   #print(prediction)
   if prediction == -1:
       print("Phishing Url")
   else:
       print("Legitimate Url")
except:
       print("Phishing Url")

