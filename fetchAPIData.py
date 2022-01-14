# Packages to import
import requests
import json
from itertools import islice

# Access the URL 
response = requests.get('https://api.publicapis.org/entries')
#print(response.json())

#store response in form of Json
data = response.json()
#file_data = response.text
'''
# Loop the JSON structure to get information for each element  
for i in data['entries']:

      #Print API, Catergory and Links information
      print("API: {}\nCATERGORY: {}\nLINKS: {}\n".format(i['API'],i['Category'],i['Link']))
'''
# Loop the JSON structure to get information with limit    
for i in islice(data['entries'], 3):
    print("API: {}\nCATERGORY: {}\nLINKS: {}\n".format(i['API'],i['Category'],i['Link']))
~                                                                                         
