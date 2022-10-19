import json
import requests

gold_response = requests.get('http://api.nbp.pl/api/cenyzlota/last/30/?format=json') #Pieprasa zelta cenas pēdējām 30 dienām

#print(response)
gold_json = json.loads(gold_response.text) #
print(gold_json)


with open('data.json', 'w') as f:
    json.dump(gold_json, f)



#print(response.status_code)
if gold_response.status_code == 200:
    print('Success!')
elif gold_response.status_code == 404:
    print('Not Found.')
#Pieprasa pēdējo 10 GBP vidējo cenu sēriju
today_res = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/gbp/last/10/?format=json')
print("—----------------------------------------------------------------------------")
today_res = json.loads(today_res.text) #
print(today_res)
with open('data_1.json', 'w') as f:
    json.dump(today_res, f)

  
print("—----------------------------------------------------------------------------")
usd_res = requests.get('https://tradestie.com/api/v1/apps/reddit', params={"sentiment": "Bearish"})
if usd_res.status_code == 200:
  print('Success!')
elif usd_res.status_code == 404:
  print('Not Found.')

usd_res_JSON = json.loads(usd_res.text) 
print(usd_res_JSON)
