import requests

url = 'http://localhost:5000/'

response = requests.get(url=url)
print(response.text)

response = requests.get(url=url+"saludar?nombre=Cristian")
print(response.text)

response = requests.get(url=url+"sumar?num1=5&num2=3")
print(response.text)

response = requests.get(url=url+"palindromo?cadena=reconocer")
print(response.text)

response = requests.get(url = url + "contar?cadena=exepciones&vocal=e")
print(response.text)