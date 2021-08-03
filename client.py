import requests
import json


txt = "Emmanuel Jean-Michel Frédéric Macron is a French politician who has been serving as the president of France since 14 May 2017."

data = json.dumps({"signature_name": "serving_default", "data": [txt,txt,txt],"dataType":"text"})
headers = {"content-type": "application/json"}
json_response = requests.post(f'http://127.0.0.1:5001/predict/model_Nlp', data=data, headers=headers)
predictions = json_response.json()
print(predictions)
#corpus = flair.datasets.WIKINER_FRENCH().downsample(0.2)
"""
for i in range(100):
    txt = corpus.test[i].to_plain_string()
    data = json.dumps({"signature_name": "serving_default", "data": [txt]})
    json_response = requests.post(f'http://0.0.0.0:5001/predict', data=data, headers=headers)
    predictions = json_response.json()
    for i in range (len(predictions["entities"])):
        print('the token is: '+ str(predictions["entities"][i]['text'])
        +', the label is ' + str(predictions["entities"][i]['labels'][0]['_value']) 
        +', with a score of '+ str(predictions["entities"][i]['labels'][0]['_score'])
        )

for _ in range(50):
    json_response = requests.post(f'http://127.0.0.1:5002/predict/Bert', data=data, headers=headers)
    json_response = requests.post(f'http://127.0.0.1:5002/predict/MobileBert', data=data, headers=headers)
    json_response = requests.post(f'http://127.0.0.1:5002/predict/XlmBert', data=data, headers=headers)
    predictions = json_response.json()
    print(predictions)
js = json_response.text 
if js:
    predictions = js
    print(predictions)
else:
    print("Error")
"""