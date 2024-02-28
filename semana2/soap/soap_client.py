from zeep import Client

client = Client('http://localhost:8000')
result = client.service.Saludar(nombre="Chris")
print(result)

x=int(input("1er numero: "))
y=int(input("2do numero: "))
result2 = client.service.SumaDosNumeros(x,y)
print(result2)

cad=input("Escriba una palabra: ") #ada #anilina
result3 = client.service.CadenaPalindromo(cad)
print(result3)