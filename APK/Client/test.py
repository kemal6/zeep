import requests

endpoint = "http://127.0.0.1/Stamp"


response = requests.get(endpoint)
print((response.status_code))
print((response.json()))

# response = requests.post(endpoint,json={
#     'lines': " Zeep SAS .."
# })

print(response.text)