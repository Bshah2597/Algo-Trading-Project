from tda import auth
import json
import config

try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path='Enter your Chrome Driver Location') as driver:
        c = auth.client_from_login_flow(
            driver, config.api_key, config.redirect_uri, config.token_path)

#Use get_quotes method to obtain stock attribute data
result = c.get_quotes("Enter your Stock Here")
#creating a temporary variable where we are storing the json list
tempMap = (json.dumps(result.json(), indent=2))
#Create another variable converting json list into object data
myMap = json.loads(tempMap)
#Storing Object data in tempStock
tempStock = myMap['Enter your Stock Here']

#Use below line to print all attributes
#print(tempStock)

#iterating through tempStock printing both key and value for desired attributes
for key, value in tempStock.items():
    if(key == 'symbol'
        or key == 'bidPrice'
        or key == 'askPrice'
        or key == 'openPrice'
        or key == 'totalVolume'):
        print(key, value)