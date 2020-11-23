import requests
import json
 
text = 'Excellent location, opposite a very large mall with wide variety of shops, restaurants and more.'

def sentiment_score(text):
	url = 'http://api.text2data.com/v3/analyze'
	payload = {
	    'DocumentText': text, 
	    'IsTwitterContent': 'false',
	    'PrivateKey': '08661BB6-5DFA-4630-9455-05F60C3E0A9D', #add your private key here (you can find it in the admin panel once you sign-up)
	    'Secret':'', #this should be set-up in admin panel as well
	    'RequestIdentifier': '' #optional, used for reporting context
	}
	 
	r = requests.post(url, data=payload)
	data=r.json()
	  
	if data['Status'] == 1:
	   print('This document is: %s%s %+.2f' % (data['DocSentimentPolarity'], data['DocSentimentResultString'],data['DocSentimentValue']))
	else: 
	   print(data['ErrorMessage'])
	    
	return data['DocSentimentResultString'], data['DocSentimentValue']