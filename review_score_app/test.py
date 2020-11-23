import requests
import json
 
url = 'http://127.0.0.1:5000/'
payload = {
    'text': 'Excellent location, opposite a very large mall with wide variety of shops, restaurants and more.'
}
 
r = requests.get(url)
print(r.status_code)
    
  
# printing the output 
