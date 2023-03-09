
import requests

url = "https://github.com/SolarCormorant/mesh/blob/main/test_bool.txt"
response = requests.get(url)
print(response.text)
