import requests
def getImageUrlFrom(query):
    endpoint = f"https://api.edamam.com/search?q={query}&app_id=68dab55a&app_key=ff337fe378ee71408ee88720420075d4&from=0&to=4"
    response = requests.get(endpoint).json()
    # response2 = requests.get(endpoint).json()
    return (response["hits"])
    # return (response["hits"][1]['recipe'])