import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = ''
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    return response.text
    
label = formatted_response["documentSentiment"]["label"]
    score = formatted_response["documentSentiment"]["score"] 
    return {'label':label, 'score': score} 
print(sentiment_analyzer("This is fun"))