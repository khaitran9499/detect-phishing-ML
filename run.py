#importing libraries
import joblib
import feature_extraction
import numpy as np
import json
#load the pickle file
classifier = joblib.load('random_forest_model.pkl')
f1 = open('dataset.csv', 'a')
f = open('data.json', 'r+')
#try:
data = json.load(f)
    
#except:
#    data = {}
#input url
url = input("Enter url:")

if url in data:
    print(data[url])
    exit()

#checking and predicting
else:
    checkprediction = feature_extraction.generate_data_set(url)
    f1.write(','.join(map(str,checkprediction)))
    checkprediction = np.array(checkprediction).reshape(1,-1)

    try:
       prediction = classifier.predict(checkprediction)
       print(prediction)
       if prediction == -1:
           data[url] = "Phishing Url"
       else:
           data[url] ="Legitimate Url"
    except:
           data[url]="Phishing Url"

    f.seek(0)
    f.write(json.dumps(data))
    f.truncate()
    f.close()
    print(data[url])
