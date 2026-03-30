# This question asks you to make a call to the dogsapi. 
# Implement the get_dog_breeds() function. 


import requests
import json
BASEURL = "https://dogapi.dog/api/v2"

def get_dog_breeds():
    """
    1) Use the GET breeds/ API endpoint at https://dogapi.dog/api/v2/breeds to fetch dog breeds. 
    2) Decode the reponse with json.loads and print out the names of all the dogs which are hypoallegenic


    API DOCS: https://dogapi.dog/docs/api-v2
    """
    
    response =requests.get(url = BASEURL + "/breeds")

    D = json.loads(response.text)

    data = D["data"]
    for i, item in enumerate(data):
        attrs = item["attributes"]
        is_hypo = bool(attrs["hypoallergenic"])
        if is_hypo:
            print(i, "\t|\t" , attrs["name"])


get_dog_breeds()



